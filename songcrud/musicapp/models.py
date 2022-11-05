from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    age = models.PositiveSmallIntegerField()

def __str__(self):
 return self.first_name

class Song(models.Model):
     title = models.CharField(max_length = 40)
     artist_id= models.ForeignKey('Artiste', on_delete=models.CASCADE)
     date_released= models.DateField(default = datetime.today)

def __str__(self):
 return self.title
class Lyrics(models.Model):
     content= models.CharField(max_length = 255)
     song_id = models.ForeignKey('Song', on_delete=models.CASCADE)
     
def __str__(self):
 return self.content