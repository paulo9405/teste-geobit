# Generated by Django 3.2.9 on 2021-11-02 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_rename_pessoateste_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='sexo',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, null=True),
        ),
    ]
