# Generated by Django 3.2.12 on 2022-02-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary_per_hour', '0008_alter_tablebody_number_of_field_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablebody',
            name='number_of_field_types',
            field=models.JSONField(default=[{'db_field_pk': 0, 'field_type': '', 'field_type_amount': 0, 'query_templates_index': 0}]),
        ),
    ]
