# Generated by Django 2.0.7 on 2018-08-21 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180821_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='nome',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
    ]
