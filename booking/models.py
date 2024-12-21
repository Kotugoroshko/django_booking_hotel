from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    location = models.TextField()

    def __str__(self):
        return f"Room #{self.number} - {self.capacity}"

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["number"]

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")  #Cascade - всі привязки видаляються; DO_NOthing - нічо не робимо, не бажаний; SET - ставимо конкретне значення; Set_Default ; PROTECT -захист від видалення
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    booking_creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.room}"
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["start_time"]
