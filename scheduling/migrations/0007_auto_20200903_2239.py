# Generated by Django 3.1.1 on 2020-09-03 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0006_auto_20200903_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduling',
            name='date',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
