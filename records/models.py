from django.db import models

# Creating a record of the pet's feed
class Record(models.Model):
    #todo auto-generate records' ID with for loop or something?
    feedID = models.CharField(max_length=100, default='0')
    # When was this record created?
    dateTime = models.DateTimeField(auto_now_add=True)
    amountLeftOver = models.IntegerField(default='0')
    amountDispensed = models.IntegerField(default='0')
    additionalInfo = models.TextField()

#python manage.py makemigrations
#python manage.py migrate

# python manage.py shell
# https://www.youtube.com/watch?v=eio1wDUHFJE - for ORM tutorial

    def __str__(self):
        return self.feedID