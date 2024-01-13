from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20, verbose_name='Жанр')

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя/Фамилия')
    info = models.URLField(blank=True)
    data = models.DateField(verbose_name='Дата рождения: ', blank=True, null=True)
    filmcount = models.IntegerField(verbose_name='Всего фильмов: ', blank=True, null=True)
    best = models.TextField(max_length=5000, verbose_name='Лучшие фильмы: ', blank=True)
    image = models.URLField(verbose_name='Фото', blank=True, null=True)
    def __str__(self):
        return self.name
    def getAbsUrl(self):
        return reverse('infodirector', args=[self.id])

class Actor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя/Фамилия')
    info = models.URLField(blank=True)
    data = models.DateField(verbose_name='Дата рождения: ', blank=True, null=True)
    filmcount = models.IntegerField(verbose_name='Всего фильмов: ', blank=True, null=True)
    image = models.URLField(verbose_name='Фото', blank=True, null=True)
    best = models.TextField(max_length=5000, verbose_name='Лучшие фильмы: ', blank=True, null=True)
    def __str__(self):
        return self.name
    def getAbsUrl(self):
        return reverse('infoactor', args=[self.id])

class Country(models.Model):
    name = models.CharField(max_length=30, verbose_name='Страна')

    def __str__(self):
        return self.name

class Podpiska(models.Model):
    VIBOR = (('free', 'БЕСПЛАТНАЯ'), ('based', 'БАЗОВАЯ'), ('super', 'ПРЕМИУМ'))
    level = models.CharField(max_length=20, choices=VIBOR, verbose_name='Подписка')

    def __str__(self):
        return self.get_level_display()

class Kino(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField(verbose_name='Год выхода')
    actors = models.ManyToManyField(Actor, verbose_name='Актеры')
    podpiska = models.ForeignKey(Podpiska, on_delete=models.SET_NULL, null=True)
    image = models.URLField(verbose_name='Изображение', blank=True)
    poster = models.URLField(verbose_name='Постер', blank=True)
    opisanie = models.TextField(max_length=2000, verbose_name='Описание', blank=True)
    trailer_url = models.URLField(verbose_name='Трейлер', null=True, unique=True, blank=True)


    def __str__(self):
        return self.title

    def displayAct(self):
        res = ''
        for one in self.actors.all():
            res += one.name + ' '
            return res

    displayAct.short_description = 'Актеры'

    def getAbsUrl(self):
        return reverse('info', args=[self.id])


class ProfiUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    podpiska = models.ForeignKey(Podpiska, on_delete=models.SET_NULL, null=True)
    balance = models.IntegerField(default=10)

    # def __str__(self):
    #     return self.user.username

class Comment(models.Model):
    # name = models.CharField(max_length=50)
    body = models.TextField(verbose_name='Напишите комментарий')
    timedata = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.body

class Video(models.Model):
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')




