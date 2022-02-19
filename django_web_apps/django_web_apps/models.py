from django.db import models
from datetime import datetime
from django.db.models import JSONField



class NameBaseModelAbstract(models.Model):
    name = models.CharField(default=None, max_length=200, blank=True)

    class Meta:
        abstract = True


class BaseModelAbstract(models.Model):
    description = models.TextField(blank=True, verbose_name='Описание', default=None)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_deleted = models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def save(self, *args, **kwargs):
        self.date_updated = datetime.now()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.date_deleted = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['date_created']


class Server(BaseModelAbstract, NameBaseModelAbstract):
    ip = models.CharField(default=None, max_length=150)
    user = models.CharField(default=None, max_length=150)
    password = models.CharField(default=None, max_length=150)
    port = models.CharField(default=None, max_length=150)
    driver = models.CharField(default=None, max_length=150)


class Db(BaseModelAbstract, NameBaseModelAbstract):
    server = models.ForeignKey('Server', on_delete=models.PROTECT, null=True)


class DbTable(BaseModelAbstract, NameBaseModelAbstract):
    db = models.ForeignKey('Db', on_delete=models.PROTECT, null=True)


class DbField(BaseModelAbstract, NameBaseModelAbstract):
    # name = models.JSONField()
    db_table = models.ForeignKey('DbTable', on_delete=models.PROTECT, null=True)


class Query(BaseModelAbstract):
    templates = JSONField(default=[])
