# Generated by Django 3.2.9 on 2021-11-02 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_pessoa_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='nascimento',
            field=models.CharField(max_length=100, null=True),
        ),
    ]