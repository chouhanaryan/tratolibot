from django.db import models

class Chats(models.Model):
    destination = models.CharField('Destination', max_length=20)
    checkin = models.DateField('Check-In', auto_now=True)
    checkout = models.DateField('Check-Out', auto_now=True)
    rooms = models.IntegerField('Rooms')