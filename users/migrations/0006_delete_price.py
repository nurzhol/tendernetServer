# Generated by Django 3.0.3 on 2020-03-01 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_profile_tarif'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Price',
        ),
    ]