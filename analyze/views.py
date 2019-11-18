from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import User, Score, Song, UserForm, ScoreForm, SongForm

# Create your views here.
class Home(ListView):
    model = User
    template_name = 'analyze/Home.html'

class Userlists(ListView):
    model = User
    context_object_name = 'userlist'
    template_name = 'analyze/user_list.html'

class Profile(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'analyze/Profile_detail.html'

def UserRegister(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/analyze/user/')
    else:
        form = UserForm
    return render(request, 'analyze/form.html', {'form': form})

class Songlists(ListView):
    model = Song
    context_object_name = 'song'
    template_name = 'analyze/Songlists.html'

class Songdetail(DetailView):
    model = Song
    context_object_name = 'song'
    template_name = 'analyze/Songdetail.html'

def SongRegister(request):
    if request.method=='POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/analyze/song')
    else:
        form = SongForm
    return render(request, 'analyze/form.html', {'form':form})

def Playdata(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    skilltable = Score.objects.order_by('-pub_date').filter(user = user.get_id())
    context = {'User' : user, 'skilltable' : skilltable}
    return render(request, 'analyze/Playdata_detail.html', context)

def ScoreRegister(request):
    if request.method=='POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
            checkOverlap()
        return redirect('/analyze')
    else:
        form = ScoreForm
    return render(request, 'analyze/form.html', {'form': form})

def Skill(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    skilltable = Score.objects.filter(user = user.get_id()).order_by('skill')[:50]
    context = {'User' : user, 'skilltable' : skilltable}
    return render(request, 'analyze/Skill.html', context)



def Versus(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    skilltable = Score.objects.filter(user = user.get_id())
    fskilltable = Score.objects.filter(user = user.rival.get_id())
    context = {'User' : user, 'skilltable' : skilltable, 'skilltables' : fskilltable}
    return render(request, 'analyze/Versus_list.html', context)

def checkOverlap():
    S = Score.objects.order_by('-pub_date')[0]
    s = Score.objects.filter(user = S.user, song = S.song).order_by('pub_date').first()
    if (S.id == s.id):
        return;
    if S.acheive > s.acheive:
        S.skill = round(s.acheive * s.song.level / 5,2)
        S.save()
        s.delete()
    else:
        S.delete()
