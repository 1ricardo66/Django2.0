# Generated by Django 2.0.7 on 2018-09-12 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180911_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Author'),
        ),
    ]