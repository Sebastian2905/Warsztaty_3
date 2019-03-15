
from django.contrib import admin
from django.urls import path

from reservation_app.views import (room_view , Create_new_room,
one_room_view, del_room_view,
edit_room_view, new_resevation,
listofroomsview, Roomfilterview, Roomdetailview)
  
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',room_view),
    path('newroom/', Create_new_room.as_view() ),
    path('specific_room/<int:my_id>/', one_room_view),
    path('del_room/<int:my_id>/', del_room_view),
    path('edit_room/<int:my_id>/', edit_room_view),
    path('new_reservation/<int:room_id>/', new_resevation),
    path('list/',listofroomsview),
    path('roomlist/',Roomfilterview.as_view()),
    path('detail/<int:pk>',Roomdetailview.as_view())
]


urlpatterns += staticfiles_urlpatterns()