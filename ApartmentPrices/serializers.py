from rest_framework import serializers
from .models import Apartment, District, Material

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ('room_no', 'area', 'h_dstr', 'h_mtrl', 'balcony',
            'total_floors', 'first_floor', 'last_floor', 'price')
        
