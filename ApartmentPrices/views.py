from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from .serializers import ApartmentSerializer
from .models import Apartment, District, Material
from .forms import ApartmentForm
import numpy as np
from .calculator import calculate

class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.order_by('-id')
    serializer_class = ApartmentSerializer

def ApartmentPrices_list(request):
	apartments = Apartment.objects.all().order_by('-id')
	return render(request, 'ApartmentPrices/ApartmentPrices_list.html', {'apartments':apartments})

def detail(request, apartment_id):
    apartment = get_object_or_404(Apartment,pk=apartment_id)
    return render(request, 'ApartmentPrices/detail.html', {'apartment': apartment})

def apartment_new(request):
    if request.method == "POST":
    	form = ApartmentForm(request.POST)
    	if form.is_valid():
            apartment = form.save(commit=False)
            apartment.save()
            return redirect('/')
    else:
    	form = ApartmentForm()
    return render(request, 'ApartmentPrices/apartment_new.html', {'form': form})
