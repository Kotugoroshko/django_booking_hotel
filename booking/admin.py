from django.contrib import admin

# Register your models here.
from booking.models import Room, Booking, Event

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Event)
