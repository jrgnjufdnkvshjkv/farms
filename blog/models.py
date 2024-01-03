from django.db import models
from django.urls import reverse
# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='about/images')
    slug = models.SlugField(max_length=100)

    def get_absolute_url(self):
        return reverse("aboutDetailView", args=[self.slug])
    def __str__(self):
        return self.name



class Features(models.Model):
    bio = models.TextField()
    img = models.ImageField(upload_to='features/images')

    def __str__(self):
        return self.name

class Team(models.Model):
    img = models.ImageField(upload_to='team/images')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    img = models.ImageField(upload_to='blog/images')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email
