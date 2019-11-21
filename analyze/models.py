from django.db import models
from django.forms import ModelForm
from django.utils import timezone
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=10)
    salutation = models.CharField(max_length=100)
    rival = models.ForeignKey('self',on_delete=models.CASCADE, blank = True, null = True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    def get_id(self):
        return self.id

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'salutation', 'rival', 'password']

class Song(models.Model):
    name = models.CharField(max_length=50)
    composer = models.CharField(max_length=50)
    level = models.FloatField()


    def __str__(self):
        return self.name

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'composer', 'level']

class Score(models.Model):
    acheive = models.FloatField()
    song = models.ForeignKey(Song,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default = timezone.now)
    skill = models.FloatField(null = True, blank = True)
    password = models.CharField(max_length = 20, null = True, blank = True)

    def __float__(self):
        return self.acheive

class ScoreForm(ModelForm):
    class Meta:
        model = Score
        fields =['acheive', 'song', 'user', 'password']
