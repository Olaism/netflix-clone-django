# Generated by Django 4.1 on 2022-11-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
