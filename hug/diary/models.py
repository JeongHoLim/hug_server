from django.db import models
from users.models import Users

# Create your models here.
class Diary(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    title = models.CharField(max_length=20,blank=True)
    content = models.CharField(max_length=100)
    result = models.IntegerField()
    happiness = models.IntegerField(default=0)
    angry = models.IntegerField(default=0)
    disgust = models.IntegerField(default=0)
    fear = models.IntegerField(default=0)
    neutral = models.IntegerField(default=0)
    sadness = models.IntegerField(default=0)
    surprise = models.IntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    counted = models.BooleanField(default=False)

    def __str__(self):
        return self.title