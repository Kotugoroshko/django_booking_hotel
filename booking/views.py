from django.shortcuts import render, redirect
from booking.models import Room, Booking, Event
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={
        "render_string":"Hello, world"
    }
    return render(request, template_name="booking/index.html", context=context)

def check_rooms():
    rooms = Room.objects.all()
    return {"rooms":rooms}

def check_event_rooms():
    rooms = Room.objects.all()
    rooms_new=[]
    for room in rooms:
        if room.capacity>10:
            rooms_new.append(room)
        
    return {"rooms":rooms_new}

def room_list(request):
    rooms = Room.objects.all()
    context={
        "rooms": rooms,
    }
    return render(request=request, template_name="booking/rooms_list.html", context=context)

def book_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room-number")
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")

        try:
            room = Room.objects.get(id = room_number)
        except ValueError:
            return HttpResponse(
                content="Wrong value for room number",
                status=400
            )
        except Room.DoesNotExist:
            return HttpResponse(
                content="This room number doesn't exists",
                status = 404
            )
        booking = Booking.objects.create(
            user = request.user,
            room = room,
            start_time = start_time,
            end_time = end_time
        )
        return redirect ("booking-details", pk=booking.id)
    else:
        return render(request, template_name="booking/booking_form.html", context=check_rooms())

def booking_details(request, pk):
    try:
        booking = Booking.objects.get(id = pk)
        context = {
            "booking":booking,
        }
        return render(request=request, template_name="booking/booking_details.html", context=context)
    except Booking.DoesNotExist:
        return HttpResponse(
            content="This booking doesn't exist",
            status = 404
        )
    

def book_event(request):

    if request.method == "POST":
        event_title = request.POST.get("event-title")
        room_number = request.POST.get("room-number")
        print(room_number)
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")

        try:
            room = Room.objects.get(id = room_number)
        except ValueError:
            return HttpResponse(
                content="Wrong value for room number",
                status=400
            )
        except Room.DoesNotExist:
            return HttpResponse(
                content="This room number doesn't exists",
                status = 404
            )
        booking = Booking.objects.create(
            user = request.user,
            room = room,
            start_time = start_time,
            end_time = end_time
        )
        event = Event.objects.create(
            title = event_title,
            booking = booking
        )
        return redirect ("event-details", pk=event.id)
    else:
        return render(request, template_name="booking/booking_event.html", context=check_event_rooms())

def event_details(request, pk):
    try:
        event = Event.objects.get(id = pk)
        context = {
            "event":event,
        }
        return render(request=request, template_name="booking/event_details.html", context=context)
    except Event.DoesNotExist:
        return HttpResponse(
            content="This event doesn't exist",
            status = 404
        )