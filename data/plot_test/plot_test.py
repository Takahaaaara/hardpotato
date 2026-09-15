from hardpotato import load_data as ld
import softpotato as sp
import matplotlib.pyplot as plt
import numpy as np

fileName = 'CA.txt'
folder = 'data/tests/CHI920D_test'

reader = ld.Read(folder, fileName)
reader.read(text='Time/sec',model='chi920d')
sp.plotting.plot(reader.x, reader.y, show=False, fig=1,
                 xlab='$t$ / s', ylab='$i$ / A',
                 fileName=folder + '/' + fileName)

fileName = 'PAC_y0.txt'
folder = 'data/tests/PAC_test'

reader = ld.Read(folder, fileName)
reader.read(text='Distance/um', model='chi920d')
sp.plotting.plot(reader.x, reader.y, show=False, fig=2,
                 xlab='$d$ / um', ylab='$i$ / A',
                 fileName=folder + '/' + fileName)

fileName = 'SECM.txt'
folder = 'data/tests/SECM_test'

reader = ld.Read(folder, fileName)
reader.read(text='X/um', model='chi920d')
x = reader.x
y = reader.y
z = reader.z[:, 0]

x_unique = np.unique(x)
y_unique = np.unique(y)

Z = z.reshape(len(y_unique), len(x_unique))

heatmap = plt.pcolormesh(
    x_unique,
    y_unique,
    Z,
    cmap='viridis'
)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('$X$ / µm', fontsize=18)
plt.ylabel('$Y$ / µm', fontsize=18)
plt.grid()
plt.tight_layout()
plt.colorbar(heatmap, label='$i$ / A')
plt.savefig(folder + '/' + fileName + '.png')
plt.close()