# Generated by Django 4.2.7 on 2023-12-10 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_kino_trailer_url_alter_actor_best_alter_actor_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='data',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения: '),
        ),
    ]