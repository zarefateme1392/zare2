# Generated by Django 3.2.8 on 2022-06-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0005_code_time2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='time2',
            field=models.FloatField(default=0),
        ),
    ]
