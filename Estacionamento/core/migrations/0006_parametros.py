# Generated by Django 2.0.7 on 2018-08-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180821_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_mes', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
