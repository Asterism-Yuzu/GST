"""Gitadora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'analyze'

urlpatterns = [
    #Home
    path('',views.Home.as_view(), name = 'title'),
    #User Lists
    path('user/',views.Userlists.as_view(), name = 'Ulists'),
    #User profile
    path('user/<int:pk>/', views.Profile.as_view(), name = 'profile'),
    #User Register
    path('user/register/', views.UserRegister, name='Uregister'),
    #Song Lists
    path('song/', views.Songlists.as_view(), name = 'Slists'),
    #Song data
    path('song/<int:pk>/', views.Songdetail.as_view(), name = 'Songdetail'),
    # Song Register
    path('song/register/', views.SongRegister, name='Sregister'),
    #Play Data
    path('user/<int:user_id>/playdata/', views.Playdata, name = 'playdata'),
    # Score Register
    path('score/register/', views.ScoreRegister, name='Lregister'),
    #Skill
    path('user/<int:user_id>/skill/', views.Skill, name = 'skill'),
    #VS
    path('user/<int:user_id>/vs', views.Versus, name = 'vs'),
]
