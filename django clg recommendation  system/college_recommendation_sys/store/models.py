from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ReviewRating(models.Model):
  
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    post = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    # usermail=models.CharField(max_length=100, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject