# Generated by Django 3.0.6 on 2020-05-15 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200514_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('message', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='prayer_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('request', models.TextField(max_length=10000)),
            ],
        ),
    ]
