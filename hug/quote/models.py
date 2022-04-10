from django.db import models

# Create your models here.

class Theme(models.Model):
    label = models.CharField(max_length=10) 
    def __str__(self):
        return self.label


class Quote(models.Model):
    content = models.CharField(max_length=1000)
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE)
    speaker = models.CharField(max_length=20,null=True,blank=True)
    # def __str__(self):
    #     return self.theme