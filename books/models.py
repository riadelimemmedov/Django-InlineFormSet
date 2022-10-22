from django.db import models
from django.urls import reverse

# Create your models here.

#!Author
class Author(models.Model):
    name = models.CharField(null=False,blank=False,max_length=255)
    last_name = models.CharField(null=True,blank=False,max_length=255)
    
    def get_absolute_url(self):
        print('Working get_absolute_url method at this class Author')
        return reverse('books:author',kwargs={'pk':self.pk})
    
    def __str__(self):
        return str(self.name)
    
#!Book
class Book(models.Model):
    title = models.CharField(null=False,blank=False,max_length=255)
    author = models.ForeignKey(Author,null=False,blank=False,on_delete=models.CASCADE,related_name='authorbook')
    
    def __str__(self):
        return f"{self.title} - {self.author}"
    
    