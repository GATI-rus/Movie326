from django.shortcuts import render
from .forms import SignUp
from .models import *
import requests
from django.http import HttpResponse
from django.views import generic
import os
import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, views


def index(req):
    items = Kino.objects.all()
    items2 = Kino.objects.filter(podpiska__level='free')
    data = {'k1': items.count(), 'k2': items2.count()}
    return render(req, 'index.html', data)


class kinolist(generic.ListView):
    model = Kino
    paginate_by = 5


# class kinodetail(generic.DetailView):
#     model = Kino

def proverka(newcom):
    blacklist = ['жопа']
    spisok = newcom.body.split()
    active = True
    for one in spisok:
        if one in blacklist:
            newcom.delete()
            active = False
    if active:
        newcom.active = True
        newcom.save()


def kinodetail(req, pk):
    film = Kino.objects.get(id=pk)
    comments = film.comment_set.filter(active=True)
    forma = CommentForm()
    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            newcom = form.save(commit=False)
            newcom.kino = film
            newcom.user = req.user
            proverka(newcom)
            form.save()
            return redirect('info', pk=pk)
    else:
        forma = CommentForm()

    data = {'kino': film, 'form': forma, 'comments': comments}
    return render(req, 'catalog/kino_detail.html', data)


class directorlist(generic.ListView):
    model = Director
    paginate_by = 5


class directordetail(generic.DetailView):
    model = Director


class actorlist(generic.ListView):
    model = Actor
    paginate_by = 5


class actordetail(generic.DetailView):
    model = Actor


def reg(req):
    if req.POST:
        f = SignUp(req.POST)
        if f.is_valid():
            f.save()
            k1 = f.cleaned_data.get('username')
            k2 = f.cleaned_data.get('password1')
            k3 = f.cleaned_data.get('email')
            k4 = f.cleaned_data.get('first_name')
            k5 = f.cleaned_data.get('last_name')

            authenticate(username=k1, password=k2)
            newuser = User.objects.get(username=k1)
            newuser.email = k3
            newuser.first_name = k4
            newuser.last_name = k5
            newuser.save()
            ProfiUser.objects.create(user_id=newuser.id, podpiska_id=1)
            login(req, newuser)
            return redirect('home')
    else:
        f = SignUp()
    data = {'forma': f}
    return render(req, 'registration/registration.html', data)


def topodpiska(req, userid):
    data = {}
    if req.POST:
        if req.POST.get('stype'):
            stype = req.POST.get('stype')
            user = User.objects.get(id=userid)
            newpodp = Podpiska.objects.get(level=stype)
            if stype == 'free':
                user.profiuser.podpiska = newpodp

            elif stype == 'based' and user.profiuser.balance >= 1:
                user.profiuser.balance -= 1
                user.profiuser.podpiska = newpodp

            elif stype == 'super' and user.profiuser.balance >= 5:
                user.profiuser.balance -= 5
                user.profiuser.podpiska = newpodp
            user.profiuser.save()

        elif req.POST.get('summa'):
            summa = req.POST.get('summa')
            print(summa)
            user = User.objects.get(id=userid)
            user.profiuser.balance += int(summa)
            user.profiuser.save()
    return render(req, 'podpiska.html', data)

# def plusbalance(req):
#     data = {}
#     return render(req, 'podpiska.html', data)


from django.shortcuts import render, redirect
from .models import *

def search_films(request):
    query = request.GET.get('query')
    if query:
        films = Kino.objects.filter(title__icontains=query)
    else:
        films = []
    return render(request, 'search.html', {'films': films})

