# Generated by Django 3.2.12 on 2022-02-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_web_apps', '0006_alter_dbfield_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbfield',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]
