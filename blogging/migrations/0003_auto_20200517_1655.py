# Generated by Django 2.1.5 on 2020-05-17 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_auto_20200517_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]