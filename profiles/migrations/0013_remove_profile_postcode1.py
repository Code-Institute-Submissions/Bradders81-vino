# Generated by Django 3.2 on 2022-03-03 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_profile_postcode1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='postcode1',
        ),
    ]