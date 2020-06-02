# Generated by Django 3.0.6 on 2020-06-02 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skilltor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('top_skilltor', models.BooleanField(default=False)),
                ('date_teaming', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
