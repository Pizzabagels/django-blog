# Generated by Django 2.1.5 on 2020-05-17 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0004_auto_20200517_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='post',
            new_name='posts',
        ),
    ]
