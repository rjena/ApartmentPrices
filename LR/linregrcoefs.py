import numpy as np

# считывание данных
'''     Лен. р-н;Окт. р-н;Прав. р-н;
        кирп.;м/к;пан.;дер.;
        этажность;1й эт.;посл. эт.;
        комн.;площадь;балкон;цена
'''
r = np.genfromtxt('/home/rjena/ApartmentPrices/LR/datawarea.csv', delimiter=';', dtype=(int, int, int, int, int, int, int, int, int, int, int, float, int, int))

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
x13 = []
x = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13]
for i in range(0,dataLen):
    y.append(r[i][varLen-1])
    for j in range(0,varLen-1):
        x[j].append(r[i][j])

# Ax = B
# A ~ (varLen,varLen) - независимые переменные
# B ~ (1,varLen) - зависимая переменная (цена)
# x ~ (1,varLen) - коэффициенты
matrB = np.zeros(varLen)
matrA = np.zeros((varLen,varLen),dtype=float)

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
invMatrA = np.linalg.pinv(matrA)
coefs = np.dot(invMatrA,matrB)

predY = np.dot(np.concatenate((np.ones((1,dataLen)),np.array(x))).T,coefs)
sse = 0
sst = 0
ym = np.mean(y)
for i in range(dataLen):
    sse += pow(predY[i] - y[i], 2)
    sst += pow(y[i] - ym, 2)
r2 = 1 - sse/sst
r2adj = 1 - (1 - r2) * (dataLen - 1) / (dataLen - varLen - 1)
print('R2 = '+'%0.2f' %r2)
print('R2adj = '+'%0.2f' %r2adj)

np.savetxt('/home/rjena/ApartmentPrices/LR/coefsLR.txt', coefs, fmt='%.15f')
