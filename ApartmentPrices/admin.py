from django.contrib import admin
from .models import Apartment, Material, District

class ApartmentAdmin(admin.ModelAdmin):
    fieldsets = [
    	('Информация о доме', {
    		'fields': ('h_dstr', 'h_mtrl', 'total_floors')
    	}),
    	('Информация о квартире', {
    		'fields': (('first_floor', 'last_floor'), 'room_no', 'area', 'balcony')
    	}),
    ]
    list_display = ('id', 'h_dstr', 'h_mtrl', 'total_floors', 'first_floor', 'last_floor', 'room_no', 'area', 'balcony', 'price')
    list_filter = ['h_dstr', 'h_mtrl']

admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Material)
admin.site.register(District)
