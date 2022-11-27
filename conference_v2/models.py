from django.contrib.auth.models import User
from django.db import models


class Presentation(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    def __str__(self):
        return f'Title: {self.title}'


class Room(models.Model):
    room_number = models.IntegerField(unique=True)

    def __str__(self):
        return f'Room: {self.room_number}'


class Schedule(models.Model):
    Schedule_Name = models.CharField(max_length=50)
    presentation_id = models.ForeignKey(Presentation, on_delete=models.SET_NULL, null=True)
    room_id = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField()
    speaker_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Schedule: {self.Schedule_Name}'






