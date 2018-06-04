import numpy as np

# считывание данных
'''     Лен. р-н;Окт. р-н;Прав. р-н;
        кирп.;м/к;пан.;дер.;
        этажность;1й эт.;посл. эт.;
        комн.;площадь;балкон;цена
'''
r = np.genfromtxt('/home/rjena/ApartmentPrices/LR/datawarea.csv', delimiter=';', dtype=(int, int, int, int, int, int, int, int, int, int, int, float, int, int))

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

yt = []
xt1 = []
xt2 = []
xt3 = []
xt4 = []
xt5 = []
xt6 = []
xt7 = []
xt8 = []
xt9 = []
xt10 = []
xt11 = []
xt12 = []
xt13 = []
xt = [xt1,xt2,xt3,xt4,xt5,xt6,xt7,xt8,xt9,xt10,xt11,xt12,xt13]

for i in range(0,len(r)):
    if i%3!=0 and i%11!=0:
        y.append(r[i][varLen-1])
        for j in range(0,varLen-1):
            x[j].append(r[i][j])
    else:
        yt.append(r[i][varLen-1])
        for j in range(0,varLen-1):
            xt[j].append(r[i][j])
            
print('Тестовое множество: '+'%.0f' %(len(yt)/len(r)*100) + '%')
# Ax = B
# A ~ (varLen,varLen) - независимые переменные
# B ~ (1,varLen) - зависимая переменная (цена)
# x ~ (1,varLen) - коэффициенты
matrB = np.zeros(varLen) #X'y
matrA = np.zeros((varLen,varLen),dtype=float) #X'X
dataLen = len(y)

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
        return np.sum(np.array(x) * np.array(x), axis = 1)
    else:
        return np.sum(np.array(x[i]) * np.array(x[j]))

getMatrixes()
coefs = np.dot(np.linalg.pinv(matrA),matrB) #b

nam = ['Ленинский','Октябрьский','Правобережный',
       'кирпич','монолит-кирпич','панель','дерево',
       'количество этажей','1й этаж','последний этаж',
       'количество комнат','площадь','балкон']
st = 'Стоимость = '+'%0.2f'%coefs[0]
for i in range(11,varLen):
    if coefs[i] < 0:
        st += ' - '+'%0.2f'%abs(coefs[i])+' * '+nam[i-1]
    else:
        st += ' + '+'%0.2f'%coefs[i]+' * '+nam[i-1]
for i in range(1,11):
    if i==1 or i==4 or i==8:
        st+='\n'
    if coefs[i] < 0:
        st += ' - '+'%0.2f'%abs(coefs[i])+' * '+nam[i-1]
    else:
        st += ' + '+'%0.2f'%coefs[i]+' * '+nam[i-1]
print(st)



testLen = len(yt)
predY = np.dot(np.concatenate((np.ones((1,testLen)),np.array(xt))).T,coefs)
sse = 0
sst = 0
ym = np.mean(yt)
for i in range(testLen):
    sse += pow(predY[i] - yt[i], 2)
    sst += pow(yt[i] - ym, 2)
r2 = 1 - sse/sst
r2adj = 1 - (1 - r2) * (testLen - 1) / (testLen - varLen - 1)
print('R2 = '+'%0.9f' %r2)
print('R2adj = '+'%0.9f' %r2adj)

np.savetxt('/home/rjena/ApartmentPrices/LR/coefsLR.txt', coefs, fmt='%.15f')
