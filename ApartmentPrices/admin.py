from django.contrib import admin
from .models import Apartment, Room, Floor, Material, District

class ApartmentAdmin(admin.ModelAdmin):
    fieldsets = [
    	('Информация о доме', {
    		'fields': ('h_dstr', 'h_mtrl')
    	}),
    	('Информация о квартире', {
    		'fields': (('ap_floor', 'first_floor', 'last_floor'), ('room_no', 'balcony'), 'price')
    	}),
    ]
    list_display = ('id', 'h_dstr', 'h_mtrl', 'ap_floor', 'first_floor', 'last_floor', 'room_no', 'balcony', 'price')
    list_filter = ['h_dstr', 'room_no', 'price']

admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Room)
admin.site.register(Floor)
admin.site.register(Material)
admin.site.register(District)
