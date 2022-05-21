from django.db import models

# Create your models here.
class FaceEmotion(models.Model):
    _date= models.DateTimeField(auto_now_add=True)
    id= models.AutoField(primary_key=True)
    image = models.ImageField(upload_to ='images/')

    def __str__(self):
        return str(self._date)