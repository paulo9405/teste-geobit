# Generated by Django 3.2.9 on 2021-11-01 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(blank=True, max_length=100)),
                ('sexo', models.CharField(max_length=100)),
                ('altura', models.IntegerField(max_length=100)),
                ('peso', models.DecimalField(decimal_places=1, max_digits=7)),
                ('nascimento', models.CharField(max_length=100)),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.bairro')),
            ],
        ),
    ]
