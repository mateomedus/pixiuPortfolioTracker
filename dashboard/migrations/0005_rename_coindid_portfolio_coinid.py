# Generated by Django 3.2.4 on 2021-08-21 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_portfolio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='coindId',
            new_name='coinId',
        ),
    ]