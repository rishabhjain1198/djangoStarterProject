from django.db import models

# Create your models here.

class Question(models.Model):
    first_name = models.CharField(max_length=30, primary_key=True)
    last_name = models.CharField(max_length=30)
    inum = models.IntegerField()
    
    def __str__(self):
        fullname = self.first_name + self.last_name
        return fullname
