import hardpotato as hp
import matplotlib.pyplot as plt
import numpy as np

folder = 'data/data/10072026/PSC_algiment_with_SECM_5'
model = 'chi920d'

xd = []
xi = []
xdata = hp.load_data.PSC('PSC_X' + '.txt', str(folder), model)
xd = xdata.d
xi = xdata.i
xi = np.array(xi)
xdi = np.diff(xi)
max_xdi = xdi.max()
min_xdi = xdi.min()
xd_max_xdi = xd[np.argmax(xdi)]
xd_min_xdi = xd[np.argmin(xdi)]
x_plateau = (xd_max_xdi - xd_min_xdi)/2 + xd_min_xdi

yd = []
yi = []
ydata = hp.load_data.PSC('PSC_y' + '.txt', str(folder), model)
yd = ydata.d
yi = ydata.i
yi = np.array(yi)
ydi = np.diff(yi)
max_ydi = ydi.max()
min_ydi = ydi.min()
yd_max_ydi = yd[np.argmax(ydi)]
yd_min_ydi = yd[np.argmin(ydi)]
y_plateau = (yd_max_ydi - yd_min_ydi)/2 + yd_min_ydi

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
