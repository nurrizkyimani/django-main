# Generated by Django 3.0.6 on 2020-06-03 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200603_1011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]