# Generated by Django 3.2.9 on 2021-11-01 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_pessoa_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='numero',
            field=models.IntegerField(null=True),
        ),
    ]
