# Generated by Django 3.2.9 on 2021-11-01 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_iden_pessoa_id_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='numero',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
