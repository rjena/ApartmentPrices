from django.shortcuts import get_object_or_404, redirect, render
from .models import Apartment
from .forms import ApartmentForm
import numpy as np

# считывание данных
'''		Лен. р-н;Окт. р-н;Прав. р-н;
		кирп.;м/к;пан.;дер.;
		этажность;1й эт.;посл. эт.;
		комн.;балкон;цена
'''
r = np.genfromtxt('/home/rjena/ApartmentPrices/data15vars.csv', delimiter=';', dtype=(int, int, int, int, int, int, int, int, int, int, int, int, float))

dataLen = len(r)    # количество квартир
varLen = len(r[0])  # количество переменных

y = []
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x9 = []
x10 = []
x11 = []
x12 = []
x = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12]
for i in range(0,dataLen):
    y.append(r[i][varLen-1])
    for j in range(0,varLen-1):
        x[j].append(r[i][j])

# Ax = B
# A ~ (varLen,varLen) - независимые переменные
# B ~ (1,varLen) - зависимая переменная (цена)
# x ~ (1,varLen) - коэффициенты
matrB = np.zeros(varLen)
matrA = np.zeros((varLen,varLen),dtype=int)

def getMatrixes():
    matrB[0] = sum(y)
    matrA[0][0] = dataLen
    diagA = summul(0,0)
    for i in range(1,varLen):
        matrB[i] = np.sum(np.array(y) * np.array(x[i-1]))
        matrA[0][i] = sum(x[i-1])
        matrA[i][0] = matrA[0][i]
        matrA[i][i] = diagA[i-1]
        for j in range(i+1,varLen):
            sumVar = summul(i-1,j-1)
            matrA[i][j] = sumVar
            matrA[j][i] = sumVar

def summul(i,j):
    if i==j:
        a = np.array(x)
        b = np.array(x)
        return np.sum(a * b, axis = 1)
    else:
        a = np.array(x[i])
        b = np.array(x[j])
        return np.sum(a * b)

getMatrixes()
invMatrA = np.linalg.inv(matrA)
coefs = np.dot(invMatrA,matrB)

def ApartmentPrices_list(request):
	apartments = Apartment.objects.all().order_by('id')
	return render(request, 'ApartmentPrices/ApartmentPrices_list.html', {'apartments':apartments})

def detail(request, apartment_id):
    apartment = get_object_or_404(Apartment,pk=apartment_id)
    return render(request, 'ApartmentPrices/detail.html', {'apartment': apartment})

def apartment_new(request):
    if request.method == "POST":
    	form = ApartmentForm(request.POST)
    	if form.is_valid():
            apartment = form.save(commit=False)
            priceCalc = coefs[0] + apartment.room_no * coefs[11] + apartment.total_floors * coefs[8]

            if apartment.balcony:
                priceCalc += coefs[12]
            if apartment.first_floor:
                priceCalc += coefs[9]
            if apartment.last_floor:
                priceCalc += coefs[10]

            if apartment.h_dstr_id<4:
                priceCalc += coefs[apartment.h_dstr_id]

            if apartment.h_mtrl_id<5:
                priceCalc += coefs[apartment.h_mtrl_id+3]

            apartment.price = priceCalc

            apartment.save()
            return redirect('/')
    else:
    	form = ApartmentForm()
    return render(request, 'ApartmentPrices/apartment_new.html', {'form': form})
