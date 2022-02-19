from django.db.models import Model
from django.contrib.auth.models import User
from django_web_apps.models import BaseModelAbstract, NameBaseModelAbstract
from django_web_apps.models import DbField
from django_web_apps.models import *


class TableBaseModelAbstract(BaseModelAbstract):
    table_num = models.IntegerField(default=0)
    row_num = models.IntegerField(default=0)
    tab_name = models.ForeignKey('Tab', on_delete=models.PROTECT, null=True)

    class Meta:
        abstract = True
        ordering = ['tab_name', 'table_num', 'row_num']


class HeaderSiderBaseModelAbstract(Model):
    column_num = models.IntegerField(default=0)
    field_value = models.CharField(blank=True, max_length=200)
    rowspan = models.IntegerField(default=1)
    colspan = models.IntegerField(default=1)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     if isinstance(self, (TableSider, TableHeader)):
    #         if self.__class__.objects.filter(table_num=self.table_num).exists():
    #             print('table_num is exists')
    #             biggest_column_num = \
    #                 self.__class__.objects.filter(table_num=self.table_num).order_by('column_num')[::-1][0].column_num
    #             if self.__class__.objects.filter(column_num=self.column_num).exists():
    #                 print('column_num is exists')
    #                 query_set = self.__class__.objects.filter(table_num=self.table_num,
    #                                                           column_num__gte=self.column_num)[::-1]
    #
    #                 for i, item in enumerate(query_set):
    #                     if item != self:
    #                         item.column_num = self.column_num + i
    #                         item.save()
    #             else:
    #                 print('column_num is not exists')
    #                 self.column_num = biggest_column_num + 1
    #
    #         else:
    #             print('table_num is not exists')
    #             self.column_num += 1
    #
    #     super().save()
    #     pass

    class Meta:
        abstract = True
        ordering = ['column_num']


class Tab(BaseModelAbstract, NameBaseModelAbstract):
    name_ru = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)


class TableBody(TableBaseModelAbstract):
    row = JSONField(default=[{
        'field_type': '',
        'field_type_amount': 0,
        'query_templates_index': 0,
        'db_field_pk': 0,
    }])


class TableHeader(TableBaseModelAbstract, HeaderSiderBaseModelAbstract):
    pass


class TableSider(TableBaseModelAbstract, HeaderSiderBaseModelAbstract):
    pass


class TableBodyFieldType(BaseModelAbstract, NameBaseModelAbstract):
    query_templates = models.ForeignKey('django_web_apps.Query', on_delete=models.PROTECT, null=True, blank=True)
