from django.urls import path,include
from . import views

app_name = "room"
urlpatterns = [
    path('',views.Rooms, name="rooms"),
    path('room/<int:id>', views.room, name="room")
    
]
