from django import forms 

from .models import Room, Reservation

class Roomform(forms.ModelForm):
    
    class Meta:
        model = Room

        fields = [
            'name',
            'seats',
            'projector'
        ]
    def clean_name(self, *args, **kwargs):
        rooms = str(Room.objects.order_by('name'))
        name = self.cleaned_data.get('name')
        if name in rooms:
            raise forms.ValidationError("Taka sala już istnieje!!!")
        else: 
            return name    

class NewRoomform(forms.ModelForm):
    
    class Meta:
        model = Room

        fields = [
            'name',
            'seats',
            'projector'
        ]
    def clean_name(self, *args, **kwargs):
        rooms = str(Room.objects.order_by('name'))
        name = self.cleaned_data.get('name')
        if name in rooms:
            raise forms.ValidationError("Taka sala już istnieje!!!")
        else: 
            return name    

class Resevationform():
    
    class Meta:
        model = Reservation

        fields = [
          'date_of_res',
          'witchroom',
          'description'
        ]