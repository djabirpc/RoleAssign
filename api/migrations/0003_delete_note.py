# Generated by Django 5.0.3 on 2024-03-27 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_role_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
    ]