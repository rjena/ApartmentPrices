import numpy as np

# считывание коэффициентов
coefs = np.loadtxt('/home/rjena/ApartmentPrices/LR/coefsLR.txt')

def calculate(d,m,tf,ff,lf,r,a,b):
    priceCalc = coefs[0] + r * coefs[11] + float(a) * coefs[12] + tf * coefs[8]

    if b:
        priceCalc += coefs[13]
    if ff:
        priceCalc += coefs[9]
    if lf:
        priceCalc += coefs[10]

    if d<4:
        priceCalc += coefs[d]

    if m<5:
        priceCalc += coefs[m+3]

    return priceCalc
