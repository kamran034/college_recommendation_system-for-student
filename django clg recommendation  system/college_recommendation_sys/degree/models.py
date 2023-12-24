from django.db import models

# Create your models here.
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField


# Create your models here.
class Postd(models.Model):
	sno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255,blank=True,null=True)
	
	image = models.ImageField(upload_to='images/%y', blank=True,null=True)
	text = RichTextField()
	date = models.DateTimeField(auto_now_add=True)
	slug = AutoSlugField(populate_from='title',null=True)


	subjecturdu= models.CharField(max_length=255,blank=True,null=True)
	subjectenglish= models.CharField(max_length=255,blank=True,null=True)
	subjectmath= models.CharField(max_length=255,blank=True,null=True)
	subjectphyics= models.CharField(max_length=255,blank=True,null=True)
	subjectchemistry= models.CharField(max_length=255,blank=True,null=True)
	subjectpakstudy= models.CharField(max_length=255,blank=True,null=True)
	subjectislmaic= models.CharField(max_length=255,blank=True,null=True)






	def __str__(self):
		return self.title
    
	





class College(models.Model):
	sno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255,blank=True,null=True)
	text = RichTextField()
	date = models.DateTimeField(auto_now_add=True)
	slug = AutoSlugField(populate_from='title',null=True, unique=True, default=None)

	def __str__(self):
		return self.title
	




	