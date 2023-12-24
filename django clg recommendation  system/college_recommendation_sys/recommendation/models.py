from django.db import models
from autoslug import AutoSlugField
# Create your models here.
from django.db import models

class Collegerecomment(models.Model):
    name = models.CharField(max_length=100,null=True,default=None)
    location = models.CharField(max_length=100,null=True,default=None)
    degree_level = models.CharField(max_length=200,null=True,default=None)
    collegelink=models.CharField(max_length=100,null=True,default=None)
    tuition_fee = models.FloatField(max_length=100,null=True,default=None)
    minimum_score = models.FloatField(max_length=100,null=True,default=None)
    
  

    def __str__(self):
        return self.name
    


class BoysCollege(models.Model):
    name = models.CharField(max_length=100,null=True,default=None)
    location = models.CharField(max_length=100,null=True,default=None)
    degree_level = models.CharField(max_length=200,null=True,default=None)
    collegelink=models.CharField(max_length=100,null=True,default=None)
    minimum_score = models.FloatField(max_length=100,null=True,default=None)
    slug = AutoSlugField(populate_from='name',null=True, unique=True, default=None)

    def __str__(self):
        return self.name

class GirlsCollege(models.Model):
    name = models.CharField(max_length=100,null=True,default=None)
    location = models.CharField(max_length=100,null=True,default=None)
    degree_level = models.CharField(max_length=200,null=True,default=None)
    collegelink=models.CharField(max_length=100,null=True,default=None)
    minimum_score = models.FloatField(max_length=100,null=True,default=None)
    slug = AutoSlugField(populate_from='name',null=True, unique=True, default=None)
    def __str__(self):
        return self.name
