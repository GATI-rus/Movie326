# Generated by Django 4.2.7 on 2023-12-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_kino_poster_alter_kino_image_alter_kino_opisanie'),
    ]

    operations = [
        migrations.AddField(
            model_name='kino',
            name='trailer_url',
            field=models.URLField(blank=True, max_length=2000, verbose_name='Трейлер'),
        ),
        migrations.AlterField(
            model_name='kino',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='podpiska',
            name='level',
            field=models.CharField(choices=[('free', 'Бесплатная'), ('based', 'Базовая'), ('super', 'Премиум')], max_length=20, verbose_name='Подписка'),
        ),
    ]
