# Generated by Django 3.2.12 on 2022-02-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_web_apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='db',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='dbfield',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='dbtable',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]
