from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ApartmentSerializer, DistrictSerializer, MaterialSerializer
from .models import Apartment, District, Material
from .forms import ApartmentForm

@api_view(['GET', 'POST'])
def apartment_api(request):
    if request.method == 'GET':
        apartment = Apartment.objects.all().order_by('-id')
        serializer = ApartmentSerializer(apartment, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def district_api(request):
    if request.method == 'GET':
        district = District.objects.all()
        d_serializer = DistrictSerializer(district, many=True)
        return Response(d_serializer.data)

@api_view(['GET'])
def material_api(request):
    if request.method == 'GET':
        material = Material.objects.all()
        m_serializer = MaterialSerializer(material, many=True)
        return Response(m_serializer.data)

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
            return redirect('/'+str(apartment.id))
    else:
    	form = ApartmentForm()
    return render(request, 'ApartmentPrices/apartment_new.html', {'form': form})
