# Generated by Django 3.2.12 on 2022-02-15 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summary_per_hour', '0010_auto_20220215_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablebody',
            old_name='number_of_field_types',
            new_name='row',
        ),
    ]
