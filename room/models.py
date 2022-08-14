from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=200)
    cretead_on = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.user.username

    class Meta:
        ordering = ('created_on',)