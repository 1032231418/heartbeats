# Generated by Django 2.0.3 on 2018-03-13 03:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('status', models.CharField(choices=[('new', 'new'), ('running', 'running'), ('stoped', 'stoped')], default='new', max_length=20)),
                ('tp', models.CharField(choices=[('at', 'at'), ('every', 'every')], default='at', max_length=20)),
                ('grace', models.IntegerField(default=30)),
                ('short_url', models.CharField(max_length=200, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'service',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.AddField(
            model_name='service',
            name='tags',
            field=models.ManyToManyField(related_name='services', to='app.Tag'),
        ),
    ]