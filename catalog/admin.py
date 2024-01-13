from django.contrib import admin
from catalog.models import *
# Register your models here.

admin.site.register(Genre)
admin.site.register(Country)



@admin.register(Actor)
class adminActor(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Director)
class adminDirector(admin.ModelAdmin):
    list_display = ('name', )
    # чтобы сделать ссылку
    # list_display_links = ('name', 'lastname')

@admin.register(Kino)
class adminKino(admin.ModelAdmin):
    list_display = ('title', 'genre', 'director', 'year', 'country', 'displayAct')
    fieldsets = (('О фильме', {'fields': ('title', 'genre', 'opisanie')}),
                 ('Люди', {'fields': ('director', 'actors')}),
                 ('Остальные', {'fields': ('country', 'year', 'podpiska', 'image', 'poster', 'trailer_url', 'likes')})
                )
    list_filter = ('genre', 'podpiska', 'year', 'country')

class PodpiskaLine(admin.StackedInline):
    model = Kino

@admin.register(Podpiska)
class adminProfileUser(admin.ModelAdmin):
    inlines = [PodpiskaLine]


@admin.register(ProfiUser)
class adminActor(admin.ModelAdmin):
    list_display = ('user', 'podpiska', 'balance')

@admin.register(Comment)
class adminComment(admin.ModelAdmin):
    list_display = ('user', 'timedata', 'kino', 'active')





