# Generated by Django 3.2.9 on 2021-11-01 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='altura',
            field=models.IntegerField(),
        ),
    ]
