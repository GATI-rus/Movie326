# Generated by Django 4.2.7 on 2023-12-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_kino_trailer_url_alter_kino_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kino',
            name='trailer_url',
        ),
        migrations.AddField(
            model_name='actor',
            name='best',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Лучшие фильмы: '),
        ),
        migrations.AddField(
            model_name='actor',
            name='filmcount',
            field=models.IntegerField(blank=True, null=True, verbose_name='Всего фильмов: '),
        ),
        migrations.AddField(
            model_name='actor',
            name='image',
            field=models.URLField(blank=True, null=True, verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='director',
            name='best',
            field=models.TextField(blank=True, max_length=200, verbose_name='Лучшие фильмы: '),
        ),
        migrations.AddField(
            model_name='director',
            name='data',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения: '),
        ),
        migrations.AddField(
            model_name='director',
            name='filmcount',
            field=models.IntegerField(blank=True, null=True, verbose_name='Всего фильмов: '),
        ),
        migrations.AddField(
            model_name='director',
            name='image',
            field=models.URLField(blank=True, null=True, verbose_name='Фото'),
        ),
    ]
