from summary_per_hour.models import TableHeader, TableBody, TableSider, TableBodyFieldType
from django_web_apps.models import DbField
from services.services_for_db import SqlHelper


class Table():

    def __init__(self):
        self.tables = {}

    def get_tables(self):
        return self.tables

    def merging_table(self, headers, bodies, siders):

        self.tables.update(headers)
        for table_num, _dict in self.tables.items():
            if table_num in _dict.keys():
                self.tables[table_num].update(siders[table_num])
                for table_num, __dict in bodies.items():

                    for row_num, _list in __dict.items():
                        column_start = len(siders[table_num]) + 1
                        for item in _list:
                            item.update(
                                {'column_start': column_start, 'column_end': column_start, 'row_start': row_num + 1,
                                 'row_end': row_num + 1})
                            self.tables[table_num][row_num].append(item)
                            column_start += 1
        print(self.tables)

    class Collector(SqlHelper.ParamBehavior):

        def __init__(self):
            SqlHelper.ParamBehavior.__init__(self)
            self.th_row_max = None
            self.bodies = {}
            self.headers = {}
            self.siders = {}
            self.tt = Table.Tool()
            self.query_set_th = None
            self.query_set_ts = None
            self.query_set_tb = None

        def get_body(self):
            return self.bodies

        def get_headers(self):
            return self.headers

        def get_siders(self):
            return self.siders

        def get_dict(self):
            if self.params:

                self.query_set_th = TableHeader.objects.filter(tab_name__name=self.params['tab_name']).order_by(
                    'column_num')
                self.query_set_ts = TableSider.objects.filter(tab_name__name=self.params['tab_name']).order_by(
                    'column_num')
                self.query_set_tb = TableBody.objects.filter(tab_name__name=self.params['tab_name']).order_by('row_num')
                self.query_sets = (self.query_set_tb, self.query_set_th, self.query_set_ts)
                self.th_row_max = self.query_set_th.order_by('-row_num')[0].row_num + 1
                for __objects in self.query_sets:
                    if isinstance(__objects[0], TableBody):
                        self.tt.collecting_dict(_objects=__objects, _dict=self.bodies, th_row_max=self.th_row_max)
                    if isinstance(__objects[0], TableHeader):
                        self.tt.collecting_dict(_objects=__objects, _dict=self.headers)
                    if isinstance(__objects[0], TableSider):
                        self.tt.collecting_dict(_objects=__objects, _dict=self.siders, th_row_max=self.th_row_max)

        def filling_body_dict(self):
            query_params = {}
            connection_params = {}
            if self.bodies:
                for i, __object in enumerate(self.query_set_tb, 0):
                    __list = []
                    # print(i, __object)
                    for row in self.bodies[__object.table_num][__object.row_num + self.th_row_max]:
                        # print(row)
                        tbft = TableBodyFieldType.objects.get(name=row['field_type'])
                        df = DbField.objects.get(pk=row['db_field_pk'])

                        query_params['query_template'] = tbft.query_templates.templates[row['query_templates_index']]
                        query_params['db_table_name'] = df.db_table.name
                        query_params['db_field_name'] = df.name

                        connection_params['server'] = df.db_table.db.server.ip
                        connection_params['driver'] = df.db_table.db.server.driver
                        connection_params['username'] = df.db_table.db.server.user
                        connection_params['password'] = df.db_table.db.server.password
                        connection_params['database'] = df.db_table.db.name
                        connection_params['port'] = df.db_table.db.server.port

                        self.tt.connection_params.update(connection_params)
                        self.tt.query_params.update(query_params)
                        data = self.tt.data_extracting()

                        for i in range(row['field_type_amount']):
                            __list.append({'value': data[0]})

                    self.bodies[__object.table_num][__object.row_num + self.th_row_max] = __list

        def filling_non_body_dict(self):
            self.tt.filling_dict(_dict=self.headers, _objects=self.query_set_th)
            self.tt.filling_dict(_dict=self.siders, _objects=self.query_set_ts, th_row_max=self.th_row_max)

        def print_params(self):

            print(self.headers)
            print(self.siders)
            print(self.bodies)

    class Tool():

        def __init__(self):
            self.sh = SqlHelper()
            self.c = self.sh.Connector()
            self.qtd = self.sh.QueryToDatabase()
            self.connection_params = {
                'server': None,
                'driver': None,
                'username': None,
                'password': None,
                'database': None,
                'port': None,
            }
            self.query_params = {
                'db_table_name': None,
                'db_field_name': None,
                'query_template': None,
            }

        def collecting_dict(self, _objects, _dict, th_row_max=None):
            if isinstance(_objects[0], (TableSider, TableBody)):
                th_row_max = th_row_max
            else:
                th_row_max = 0
            for __object in _objects:
                if __object.table_num not in _dict.keys():
                    _dict.update({__object.table_num: {}})
                if hasattr(__object, 'row'):
                    _dict[__object.table_num].update(
                        {__object.row_num + th_row_max: __object.row})
                else:
                    _dict[__object.table_num].update({__object.row_num + th_row_max: []})

        def data_extracting(self):
            self.c.set_params(**self.connection_params)
            self.qtd.set_params(**self.query_params)
            cn = self.c.set_connection_to_database()
            query = self.qtd.get_query_to_database()
            data = self.sh.get_data_from_db(query_to_database=query, cn=cn)
            return data[0]

        def filling_dict(self, _objects, _dict, th_row_max=None):
            print(_objects)
            column_start = 1
            if th_row_max:
                th_row_max = th_row_max
            else:
                th_row_max = 0

            for i, __object in enumerate(_objects, 1):
                _dict[__object.table_num][__object.row_num + th_row_max].append(
                    {'value': __object.field_value, 'column_start': __object.column_num,
                     'column_end': __object.column_num + 0 if __object.colspan == 1 else __object.column_num + __object.colspan - 1,
                     'row_start': __object.row_num + th_row_max + 1,
                     'row_end': __object.row_num + th_row_max + __object.rowspan, 'colspan': __object.colspan,
                     'rowspan': __object.rowspan})
                column_start += __object.column_num
