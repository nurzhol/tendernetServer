# Generated by Django 3.0.3 on 2020-02-12 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0004_article_favourite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Лот', 'verbose_name_plural': 'Лоты'},
        ),
    ]
