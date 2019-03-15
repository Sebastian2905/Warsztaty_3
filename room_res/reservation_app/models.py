from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=64)
    seats = models.IntegerField()
    projector = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Reservation(models.Model):
    date_of_res = models.DateField()
    witch_room = models.ForeignKey(Room, on_delete = models.CASCADE)
    description = models.TextField(max_length=500)
    def __str__(self):
        return str(self.date_of_res)+"-"+str(self.witch_room)