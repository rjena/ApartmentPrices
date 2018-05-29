from rest_framework import serializers
from .models import Apartment, District, Material

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ('room_no', 'area', 'h_dstr', 'h_mtrl', 'balcony',
            'total_floors', 'first_floor', 'last_floor', 'price')
    def validate(self, data):
        if data['area'] < data['room_no'] * 10:
            raise serializers.ValidationError('Площадь должна быть не меньше значения: Количество комнат * 10 !')
        if data['total_floors'] == 2 and not(data['first_floor']) and not(data['last_floor']):
            raise serializers.ValidationError('Всего этажей вы выбрали 2. Отметьте первый или последний этаж !')
        if data['total_floors'] == 1 and (data['first_floor'] or data['last_floor']):
            raise serializers.ValidationError('Всего этажей вы выбрали 1. Уберите отметки у первого и последнего этажа !')
        if data['first_floor'] and data['last_floor']:
            raise serializers.ValidationError('Вы выбрали и первый, и последний этаж. Отметьте один вариант !')
        return data

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('name_dstr',)

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('name_mtrl',)
