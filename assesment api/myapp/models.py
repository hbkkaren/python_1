from django.db import models

# Create your models here.
class Book(models.Model):
	title=models.CharField(max_length=100,blank=True)
	code=models.CharField(max_length=100,blank=True)
	language=models.CharField(max_length=100,blank=True)
	style=models.CharField(max_length=100,blank=True)

	def __str__(self):
		return self.title

