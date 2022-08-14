from django.shortcuts import render
from .models import Room,Message
from django.contrib.auth.decorators import login_required




@login_required
def Rooms(request):
    rooms = Room.objects.all()

    context ={
        "rooms":rooms
    }

    return render(request, 'room/rooms.html', context)


@login_required
def room(request,id):
    room = Room.objects.get(pk=id)
    messages = Message.objects.all()
    context ={
        'room':room,
        'messages':messages,
    }

    return render(request,'room/room.html', context)
