# Generated by Django 3.2.12 on 2022-02-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_web_apps', '0005_rename_query_to_db_list_querytodb_queries_to_db_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbfield',
            name='name',
            field=models.JSONField(),
        ),
    ]
