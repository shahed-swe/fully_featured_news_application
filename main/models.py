from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Main(models.Model):
    name = models.SlugField(max_length=20)
    fb = models.CharField(max_length = 100,null=True)
    tw = models.CharField(max_length = 100,null=True)
    ln = models.CharField(max_length = 100,null=True)
    yt = models.CharField(max_length = 100,null=True)

    def __str__(self):
        return self.name

class fooAbout(models.Model):
    about1 = models.TextField()
    about2 = models.TextField()

    def __str__(self):
        return self.about1 + self.about2
    