# Generated by Django 2.2.3 on 2020-03-09 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_item',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='modified_item',
            new_name='modified_time',
        ),
    ]
