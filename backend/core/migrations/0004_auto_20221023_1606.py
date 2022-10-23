# Generated by Django 2.2.16 on 2022-10-23 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20221023_1528'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='recipe',
            constraint=models.UniqueConstraint(fields=('author', 'name'), name='unique_recipe'),
        ),
    ]
