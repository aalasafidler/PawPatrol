from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Record(models.Model):
    feedID = models.AutoField(primary_key=True)
    dateTime = models.DateTimeField(auto_now_add=True)
    amountLeftOver = models.IntegerField(default='0')
    amountDispensed = models.IntegerField(default='0')
    additionalInfo = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

class Pet(models.Model):
    petName = models.CharField(max_length=100, default='My Pet')
    petImage = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)



















    #author = models.CharField(max_length=100, default=settings.AUTH_USER_MODEL)

    #def __str__(self):
    #    return self.petName



    #python manage.py makemigrations
#python manage.py migrate

# python manage.py shell
# https://www.youtube.com/watch?v=eio1wDUHFJE - for ORM tutorial
    """from records.models import Pet
    Pet.objects.all()
    pet1 = Pet()
    pet1.petName = "Roger"
    pet1.save()
        #
    thumb = models.ImageField(default='default.png', blank=True)"""


    #def __str__(self):
        #return self.feedID
