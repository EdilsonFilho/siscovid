# Generated by Django 3.1.1 on 2020-09-02 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0004_scheduling_querycovid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduling',
            name='querycovid',
        ),
    ]
