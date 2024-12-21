from django.contrib import admin

# Register your models here.
from booking.models import Room, Booking

admin.site.register(Room)
admin.site.register(Booking)