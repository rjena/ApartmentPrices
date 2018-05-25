from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ApartmentSerializer
from .models import Apartment
from .forms import ApartmentForm

@api_view(['GET', 'POST'])
def apartment_api(request):
    if request.method == 'GET':
        apartment = Apartment.objects.latest('id')
        serializer = ApartmentSerializer(apartment)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def ApartmentPrices_list(request):
	apartments = Apartment.objects.all().order_by('-id')
	return render(request, 'ApartmentPrices/ApartmentPrices_list.html', {'apartments':apartments})

def detail(request, apartment_id):
    apartment = get_object_or_404(Apartment,pk=apartment_id)
    return render(request, 'ApartmentPrices/detail.html', {'apartment': apartment})

def apartment_new(request):
    if request.method == 'POST':
    	form = ApartmentForm(request.POST)
    	if form.is_valid():
            apartment = form.save(commit=False)
            apartment.save()
            return redirect('/')
    else:
    	form = ApartmentForm()
    return render(request, 'ApartmentPrices/apartment_new.html', {'form': form})
