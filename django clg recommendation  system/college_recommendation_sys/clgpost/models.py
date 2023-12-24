from django.db import models

# Create your models here.


from autoslug import AutoSlugField
from ckeditor.fields import RichTextField



class Collegepost(models.Model):
	sno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255,blank=True,null=True)
	text = RichTextField()
	date = models.DateTimeField(auto_now_add=True)
	slug = AutoSlugField(populate_from='title',null=True, unique=True, default=None)

	meritFSCE =models.IntegerField(null=True,default=None)
	meritFSCM =models.IntegerField(null=True,default=None)
	meritICSC =models.IntegerField(null=True,default=None)
	meritICSS =models.IntegerField(null=True,default=None)
	meritICSE =models.IntegerField(null=True,default=None)
	meritCOM =models.IntegerField(null=True,default=None)
	collegelink = models.CharField(max_length=255,blank=True,null=True)


    # meritFSC=

	
	def __str__(self):
		return self.title


class Comment(models.Model):
	sno = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255,blank=True,null=True)
	email = models.CharField(max_length=255,blank=True,null=True)
	post = models.ForeignKey(Collegepost,on_delete=models.CASCADE,null=True,blank=True)
	message = models.TextField(max_length=500, blank=True)

	def __str__(self):
		return self.name
