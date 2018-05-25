import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
# считывание данных
'''		Лен. р-н;Окт. р-н;Прав. р-н;
		кирп.;м/к;пан.;дер.;
		этажность;1й эт.;посл. эт.;
		комн.;балкон;цена
'''
names = ['lenin','okt','prav',
         'kirp','mk','pan','der',
         'floors','1st','last',
         'rooms','area','balcony','price']
r = np.genfromtxt('/home/rjena/ApartmentPrices/LR/datawarea.csv', delimiter=';', names=names,
                  dtype=(int, int, int,
                         int, int, int, int,
                         int, int, int,
                         int, float, int, int))

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
xx = np.transpose(x)
model = ExtraTreesClassifier()

model.fit(xx, y)

print(model.feature_importances_)
