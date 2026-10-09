import hardpotato as hp
import numpy as np
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

model = 'chi920d'
path = 'C:/Users/parasita/Downloads/chi920d/chi920d.exe'
date_str = datetime.now().strftime("%m%d%Y")
tech = 'PSC_algiment_with_SECM'
folder= Path(f'data/data/{date_str}/{tech}') 
Path.mkdir(folder, parents=True, exist_ok=True)

E1 = 0.4
sesns1 = 1e-9

hp.potentiostat.Setup(model, path, str(folder))
secm = hp.potentiostat.SECM()

x_position = 0
y_position = 0
print('X position:', x_position)
print('Y position:', y_position)


dist = 500
secm.PSC(E1=E1, sens=sesns1, qt=30, dir='x', dist=dist, incrdist=0.25, incrtime=0.05, fileName='PSC_X', header='PSC_test')
secm.RUN()
x_position = x_position + dist
print('X position:', x_position)
print('Y position:', y_position)

xd = []
xi = []
xdata = hp.load_data.PSC('PSC_X' + '.txt', str(folder), model)
xd = xdata.d
xi = xdata.i
xi = np.array(xi)
xdi = np.diff(xi)
xddi = np.diff(xdi)
xd_xddimax = xd[np.argmax(xddi)]

max_xdi = xdi.max()
min_xdi = xdi.min()

xd_max_xdi = xd[np.argmax(xdi)]
xd_min_xdi = xd[np.argmin(xdi)]

x_plateau = (xd_max_xdi - xd_min_xdi)/2 + xd_min_xdi


secm.MOVE(x=x_plateau - x_position, y=-300)
x_position = x_position + (x_plateau - x_position)
y_position = y_position -300
print('X position:', x_position)
print('Y position:', y_position)
dist = 500
secm.PSC(E1=E1, sens=sesns1, qt=30, dir='y', dist=dist, incrdist=0.25, incrtime=0.05, fileName='PSC_y', header='PSC_test')
secm.RUN()
y_position = y_position + dist
print('X position:', x_position)
print('Y position:', y_position)

yd = []
yi = []
ydata = hp.load_data.PSC('PSC_y' + '.txt', str(folder), model)
yd = ydata.d
yi = ydata.i
yi = np.array(yi)
ydi = np.diff(yi)
yddi = np.diff(ydi)
yd_yddimax = yd[np.argmax(yddi)]

max_ydi = ydi.max()
min_ydi = ydi.min()

yd_max_ydi = yd[np.argmax(ydi)]
yd_min_ydi = yd[np.argmin(ydi)]

y_plateau = (yd_max_ydi - yd_min_ydi)/2 + yd_min_ydi

secm.MOVE(x=-125, y=(y_plateau - y_position)+125)
# secm.MOVE(y=(y_plateau - y_position))
y_position = y_position + (y_plateau - y_position)
print('X position:', x_position)
print('Y position:', y_position)
secm.SECM(E1=E1, sens=sesns1, xdist=250, ydist=-250, incrdist=2, incrtime=0.01, fileName='SECM_final')
# secm.CV(Eini=0, Ev1=0, Ev2=0.4, Efin=0.4, sens=1e-9, nSweeps=4, E2=0.4, sens2=1e-8)
secm.RUN()

fig, ax = plt.subplots(2, 2, figsize=(12, 6))
ax = ax.flatten()

ax[0].plot(xd, xi)
xd = xd[1:]
ax[1].plot(xd, xdi)
ax[1].set_title('PSC X [di, x]')

ax[0].axvline(x=xd_max_xdi)
ax[0].axvline(x=xd_min_xdi)
ax[0].axvline(x=x_plateau, color='r')
ax[0].set_title('PSC X')

ax[2].plot(yd, yi)
yd = yd[1:]
ax[3].plot(yd, ydi)
ax[3].set_title('PSC y [di, y]')

ax[2].axvline(x=yd_max_ydi)
ax[2].axvline(x=yd_min_ydi)
ax[2].axvline(x=y_plateau, color='r')
ax[2].set_title('PSC Y')

plt.tight_layout()
plt.show()
