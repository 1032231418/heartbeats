# Generated by Django 2.0.3 on 2018-03-13 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180313_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='short_url',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]