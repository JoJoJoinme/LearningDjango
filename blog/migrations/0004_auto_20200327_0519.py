# Generated by Django 2.2.3 on 2020-03-26 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200327_0514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='excert',
            new_name='excerpt',
        ),
    ]
