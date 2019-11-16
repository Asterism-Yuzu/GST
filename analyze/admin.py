from django.contrib import admin
from .models import User, Song, Score

# Register your models here.

admin.site.register(User)
admin.site.register(Song)
admin.site.register(Score)