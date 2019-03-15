from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Template
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DeleteView
from django.views import View
from .models import Room, Reservation
import datetime
from .filters import RoomFilters

from .forms import Roomform, NewRoomform

class Roomfilterview(ListView):
    template_name = 'room_list.html'
    queryset = Room.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RoomFilters(self.request.GET,queryset=self.get_queryset()) 
        return context
    
class Roomdetailview(DeleteView):
    template_name = 'room_detail.html'
    queryset = Room.objects.all() 

def room_view(request): 
    today = datetime.date.today()
    days = [today + datetime.timedelta(i) for i in range(7)]

    all_rooms = Room.objects.order_by('name')
    all_booking = Reservation.objects.all()

    
                      

    mydata ={
        "all_rooms": all_rooms,
        "bookings": all_booking,
        "days": days,
    
    }


    
    return render(request,"content.html", mydata)
   

class Create_new_room(View):
    def get(self,request):
        form = Roomform()

        context={
        'form':form
        }
           
        return render(request,"form.html",context)
    def post(self,request):
        form = Roomform(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponse("Dodano nową salę")  
        return render(request,"form.html",{"form":form})


def one_room_view(request, my_id):
    today = datetime.date.today()

    specific_room = Room.objects.get(id = my_id)
    res_of_room = Reservation.objects.filter(witch_room=specific_room)

    
    data = {
        "specific_room" : specific_room,
        "res_of_room" : res_of_room,
        "today" : today,
        "id" : my_id,

    }

    return render(request,"room.html", data )


def del_room_view(request, my_id):
    nameofroom = str(Room.objects.get(id = my_id).name)
    Room.objects.get(id = my_id).delete()
    

    
    data = {
        "nameofroom" : nameofroom,
    
    }

    return render(request,"del.html", data )


def edit_room_view(request, my_id):
    instance = get_object_or_404(Room, id=my_id)
    form = NewRoomform(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponse("Zaktualizowano salę!")

    return render(request,"edit.html", {"form": form} )


def new_resevation(request,room_id):
    today = datetime.date.today()
    print(today)
    current_room=Room.objects.get(id = room_id)
    all_res = current_room.reservation_set.all()
    if request.method == "POST":
        r_date = request.POST['mydate']
        r_date=datetime.datetime.strptime(r_date, '%Y-%m-%d').date()
        r_desc = request.POST['description']
        if r_date <= today:
             return HttpResponse("Zła data. Nie możesz wybrać daty z przeszłości!")
        for book in all_res:
            if book.date_of_res == r_date:
                return HttpResponse("Ta sala została już zarezerwowana w tym terminie!")     
        obj = Reservation.objects.create(date_of_res = r_date, witch_room = current_room,description = r_desc)
        obj.save()
        return HttpResponse("Ok nowa rezerwacja")
  
    return render(request,"to_book.html", {"nazwa":current_room.name} )     
     
def listofroomsview(request):
    roomlist = Room.objects.all()
    if request.method =="POST":
       # s_name = request.GET['myname']
        s_proj = request.POST['projector']
        roomlist = Room.objects.filter(projector==s_proj)
    
    

    content = {
        "roomlist":roomlist 
    }
    return render(request,"filter.html",content)



    