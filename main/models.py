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
        return self.name + " | " + str(self.pk)

class fooAbout(models.Model):
    about1 = models.TextField()
    about2 = models.TextField()
    telephone = models.TextField(default="(+880)")

    def __str__(self):
        return "About No | " + str(self.pk)

class about_main(models.Model):
    about_first = models.TextField(default="-")
    about_second = models.TextField(default="-")
    about_third = models.TextField(default="-")

    def __str__(self):
        return (self.about_first[0:10]) + " | " + str(self.pk)