# Generated by Django 4.2.7 on 2023-12-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_kino_image_alter_kino_opisanie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='director',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Имя/Фамилия'),
        ),
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Имя/Фамилия'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='kino',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='podpiska',
            name='level',
            field=models.CharField(choices=[('free', 'free'), ('based', 'based'), ('super', 'super')], max_length=20, verbose_name='Подписка'),
        ),
    ]
