# Generated by Django 3.0.3 on 2020-02-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0007_auto_20200214_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='down',
            field=models.FileField(null=True, upload_to='media/', verbose_name='Документы для закгрузки'),
        ),
    ]
