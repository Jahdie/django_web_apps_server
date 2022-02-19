# Generated by Django 3.2.12 on 2022-02-13 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_web_apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=200)),
                ('description', models.TextField(blank=True, default=None, verbose_name='Описание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name_ru', models.CharField(blank=True, max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableSider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default=None, verbose_name='Описание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('table_num', models.IntegerField(default=0)),
                ('row_num', models.IntegerField(default=0)),
                ('column_num', models.IntegerField(default=0)),
                ('field_value', models.CharField(blank=True, max_length=200)),
                ('rowspan', models.IntegerField(default=1)),
                ('colspan', models.IntegerField(default=1)),
                ('tab_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='summary_per_hour.tab')),
            ],
            options={
                'ordering': ['tab_name', 'table_num', 'row_num'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default=None, verbose_name='Описание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('table_num', models.IntegerField(default=0)),
                ('row_num', models.IntegerField(default=0)),
                ('column_num', models.IntegerField(default=0)),
                ('field_value', models.CharField(blank=True, max_length=200)),
                ('rowspan', models.IntegerField(default=1)),
                ('colspan', models.IntegerField(default=1)),
                ('tab_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='summary_per_hour.tab')),
            ],
            options={
                'ordering': ['tab_name', 'table_num', 'row_num'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableBodyFieldType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default=None, verbose_name='Описание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('table_head_field_type', models.CharField(max_length=200)),
                ('query_to_db', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='django_web_apps.querytodb')),
            ],
            options={
                'ordering': ['date_created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default=None, verbose_name='Описание')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('table_num', models.IntegerField(default=0)),
                ('row_num', models.IntegerField(default=0)),
                ('number_of_field_types', models.JSONField()),
                ('tab_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='summary_per_hour.tab')),
            ],
            options={
                'ordering': ['tab_name', 'table_num', 'row_num'],
                'abstract': False,
            },
        ),
    ]