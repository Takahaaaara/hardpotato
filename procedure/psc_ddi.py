import hardpotato as hp
import numpy as np
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

model = 'chi920d'
path = 'C:/Users/parasita/Downloads/chi920d/chi920d.exe'
date_str = datetime.now().strftime("%m%d%Y")
tech = 'PSC_ddi'
folder= Path(f'data/data/{date_str}/{tech}') # NOTE: verificar se isso funciona
Path.mkdir(folder, parents=True, exist_ok=True)

hp.potentiostat.Setup(model, path, str(folder))
secm = hp.potentiostat.SECM()

secm.MOVE(x=-300)
dist = 500
secm.PSC(E1=0.4, sens=1e-9, qt=30, dir='x', dist=dist, incrdist=0.5, incrtime=0.05, fileName='PSC_X', header='PSC_test')
# secm.RUN()

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

plateau = (xd_max_xdi - xd_min_xdi)/2 + xd_min_xdi

print('x at di Min:', xd_min_xdi)

print('x at di Max:', xd_max_xdi)



fig, ax = plt.subplots(2, 1, figsize=(12, 6))
ax[0].plot(xd, xi)
xd = xd[1:]
ax[1].plot(xd, xdi)

ax[0].axvline(x=xd_max_xdi)
ax[0].axvline(x=xd_min_xdi)
ax[0].axvline(x=plateau, color='r')



plt.show()
