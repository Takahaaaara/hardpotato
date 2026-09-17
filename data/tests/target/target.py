import hardpotato as hp
import numpy as np


model = 'chi920d'
path = 'C:/Users/parasita/Downloads/chi920d/chi920d.exe'
folder = 'data/tests/target'

hp.potentiostat.Setup(model, path, folder)
secm = hp.potentiostat.SECM()

x_position = 0
y_position = 0

print('X position:', x_position)
print('Y position:', y_position)
secm.PAC(E1=0.4, qt = 30, sens=1e-8, maxincr=0.5, iratio=75, fileName='PAC', header='PAC_test', withdraw=100)
#secm.RUN()
dist = 500
secm.PSC(E1=0.4, sens=1e-8, qt=30, dir='x', dist=dist, incrdist=0.5, incrtime=0.05, fileName='PSC_X', header='PSC_test')
#secm.RUN()
x_position = x_position + dist
print('X position:', x_position)
print('Y position:', y_position)

xi = []
xd = []
xdata = hp.load_data.PSC('PSC_X' + '.txt', folder, model)
xi = xdata.i
xi = np.array(xi)
ximax = np.max(abs(xi))
xd = xdata.d
xd_imax = xd[np.argmax(abs(xi))]
print(ximax)
print('max current in X:', xd_imax)

secm.MOVE(x= xd_imax - x_position)
x_position = x_position + (xd_imax - x_position)
print('X position:', x_position)
print('Y position:', y_position)
dist = -500
secm.PSC(E1=0.4, sens=1e-8, qt=30, dir='y', dist=dist, incrdist=0.5, incrtime=0.05, fileName='PSC_Y', header='PSC_test')
#secm.RUN()
y_position = y_position + dist
print('X position:', x_position)
print('Y position:', y_position)

yi = []
yd = []
ydata = hp.load_data.PSC('PSC_Y' + '.txt', folder, model)
yi = ydata.i
yi = np.array(yi)
yimax = np.max(abs(yi))
yd = ydata.d
yd_imax = yd[np.argmax(abs(yi))]
print(yimax)
print('max current in Y:', yd_imax)

secm.MOVE(y= yd_imax - y_position)
y_position = y_position + (yd_imax - y_position)
print('X position:', x_position)
print('Y position:', y_position)
secm.CV(Eini=0, Ev1=0.4, Ev2=0, Efin=0, sr=0.1, sens=1e-8, fileName='CV_maxi')
#secm.RUN()
