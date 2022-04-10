from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=10)
    happiness = models.IntegerField(default=0)
    angry = models.IntegerField(default=0)
    disgust = models.IntegerField(default=0)
    fear = models.IntegerField(default=0)
    neutral = models.IntegerField(default=0)
    sadness = models.IntegerField(default=0)
    surprise = models.IntegerField(default=0)

    def __str__(self):
        return self.nick_name
