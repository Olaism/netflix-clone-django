# Generated by Django 4.1 on 2022-11-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
