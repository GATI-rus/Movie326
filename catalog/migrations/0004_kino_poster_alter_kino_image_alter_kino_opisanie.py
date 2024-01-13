# Generated by Django 4.2.7 on 2023-12-09 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_actor_lastname_remove_director_lastname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kino',
            name='poster',
            field=models.URLField(blank=True, verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='kino',
            name='image',
            field=models.URLField(blank=True, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='kino',
            name='opisanie',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Описание'),
        ),
    ]
