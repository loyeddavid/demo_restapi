from django.db import models
class Question(models.Model):
    title=models.TextField(null=True,blank=True)
    status=models.CharField(default='inactive',max_length=10)

# Create your models here.
