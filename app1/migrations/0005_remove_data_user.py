# Generated by Django 2.1.7 on 2019-03-15 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_data_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='user',
        ),
    ]
