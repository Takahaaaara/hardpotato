import hardpotato as hp
import numpy as np
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

model = 'chi920d'
path = 'C:/Users/parasita/Downloads/chi920d/chi920d.exe'
date_str = datetime.now().strftime("%m%d%Y")
folder= Path(f'data/data/{date_str}') # NOTE: verificar se isso funciona
Path.mkdir(folder, parents=True, exist_ok=True)
# folder = f'data/data/{today}'

hp.potentiostat.Setup(model, path, str(folder))
secm = hp.potentiostat.SECM()

secm.PAC(E1=0.4, qt = 30, sens=1e-8, maxincr=0.5, iratio=75, fileName='PAC', header='PAC_test', withdraw=100)
secm.RUN()
dist = 500
secm.PSC(E1=0.4, sens=1e-8, qt=30, dir='x', dist=dist, incrdist=0.5, incrtime=0.05, fileName='PSC_X', header='PSC_test')
secm.RUN()
xd = []
xdata = hp.load_data.PSC('PSC_X' + '.txt', str(folder), model)
xi = xdata.i
xi = np.array(xi)
xdi = np.diff(xi)
xddi = np.diff(xdi)

fig, ax = plt.subplots(1, 3, figsize=(6, 10))
ax[0].plot(xd, xi)
ax[1].plot(xd, xdi)
ax[2].plot(xd, xddi)

plt.show()