# Generated by Django 2.0.7 on 2018-09-12 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180911_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='author',
            field=models.CharField(max_length=60),
        ),
    ]
