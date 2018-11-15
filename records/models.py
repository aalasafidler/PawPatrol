from django.db import models
from django.contrib.auth.models import User

# Creating a record of the pet's feed
class Record(models.Model):
    #todo auto-generate records' ID with for loop or something?
    feedID = models.AutoField(primary_key=True)
    #feedID = models.CharField(max_length=100, default='0')
    # When was this record created?
    dateTime = models.DateTimeField(auto_now_add=True)
    amountLeftOver = models.IntegerField(default='0')
    amountDispensed = models.IntegerField(default='0')
    additionalInfo = models.TextField()
    """thumb = models.ImageField(default='default.png', blank=True)"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

#python manage.py makemigrations
#python manage.py migrate

# python manage.py shell
# https://www.youtube.com/watch?v=eio1wDUHFJE - for ORM tutorial
    """from records.models import Pet
    Pet.objects.all()
    pet1 = Pet()
    pet1.petName = "Roger"
    pet1.save()
    """

    def __str__(self):
        return self.feedID

# Adding a new pet
class Pet(models.Model):
    petName = models.CharField(max_length=100, default='My Pet')
    # When was this record created?
    petImage = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.petName
