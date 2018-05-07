from django import forms

from .models import Apartment

class ApartmentForm(forms.ModelForm):

    class Meta:
        model = Apartment
        fields = ('room_no', 'h_dstr', 'h_mtrl',
                  'balcony', 'total_floors',
                  'first_floor', 'last_floor',)
