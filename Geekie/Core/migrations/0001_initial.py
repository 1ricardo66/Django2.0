# Generated by Django 2.0.7 on 2018-09-29 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=120)),
                ('data_de_nascimento', models.DateField()),
                ('senha', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Cpf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
        migrations.AddField(
            model_name='cadastro',
            name='cpf',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Core.Cpf'),
        ),
    ]
