import pyodbc

class SqlHelper:
    def __init__(self):
        self.cn = None
        self.data = None
        self.query_to_database = None

    def get_data_from_db(self, query_to_database, cn):
        self.query_to_database = query_to_database
        self.cn = cn
        cursor = cn.cursor()
        cursor.execute(query_to_database)

        self.data = cursor.fetchmany(1)
        return self.data


    class ParamBehavior:
        def __init__(self):
            self.params = {}
            self.kwargs = {}


        def set_params(self, **kwargs):
            for key, value in kwargs.items():
                self.params.update({key: value})
            # print(self.params)


    class Connector(ParamBehavior):
        params = {}

        def __init__(self):
            SqlHelper.ParamBehavior.__init__(self)
            self.cn = None


        def set_connection_to_database(self):
            connection_string = ""
            for key, value in self.params.items():
                connection_string += f"{key}={value};"

            try:
                # print(connection_string)
                self.cn = pyodbc.connect(connection_string)
                return self.cn
            except:
                print("Error connect to db!")


    class QueryToDatabase(ParamBehavior):
        params = {}

        def __init__(self):
            SqlHelper.ParamBehavior.__init__(self)
            self.query_to_database = None
            self.data_from_database = None


        def get_query_to_database(self):
            query_template = f"{self.params['query_template']}"
            self.query_to_database = query_template.format(**self.params)
            # print(self.query_to_database)
            return self.query_to_database

