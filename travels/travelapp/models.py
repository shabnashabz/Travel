from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=255)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    
    def __str__(self):
        return self.name
class photo(models.Model):
    names=models.CharField(max_length=255)
    imgs=models.ImageField(upload_to='picture')
    descs=models.TextField()
    
    def __str__(self):
        return self.names