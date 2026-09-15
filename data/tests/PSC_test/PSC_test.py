import hardpotato as hp
import numpy as np


model = 'chi920d'
path = 'C:/Users/parasita/Downloads/chi920d/chi920d.exe'
folder = 'data/tests/PSC_test'

print(hp.potentiostat.models_available)
info = hp.potentiostat.Info(model)
info.specifications()

hp.potentiostat.Setup(model, path, folder)
secm = hp.potentiostat.SECM()
position = 0
print('actual position:', position)
secm.PAC(E1=0.4, qt = 30, sens=1e-8, maxincr=0.5, iratio=60, fileName='PAC', header='PAC_test', withdraw=100)
secm.RUN()
dist = -500
secm.PSC(E1=0.4, sens=1e-8, qt=30, dir='x', dist=dist, incrdist=0.5, incrtime=0.05, fileName='PSC', header='PSC_test')
secm.RUN()
position = position + dist
print('actual position:', position)

i = []
d = []
data = hp.load_data.PSC('PSC' + '.txt', folder, model)

i = data.i
i = np.array(i)
imax = np.max(abs(i))
d = data.d
d_imax = d[np.argmax(abs(i))]
print(imax)
print('max current in:', d_imax)

secm.MOVE(x=position-d_imax)
secm.CV(Eini=0, Ev1=0.4, Ev2=0, Efin=0, sr=0.1, sens=1e-8, fileName='CV_maxi')
secm.RUN()
position = position + (position-d_imax)
print('actual position:', position)

# E2List = [0, 0.4, -0.4]
# for E2 in E2List:
#     secm.MOVE('step', z=-150)
#     secm.PSC(E1=0.4, dist=150, qt=30, E2=E2, sens2=1e-4,sens=1e-8, fileName=f'PSC_E2_{E2}', header=f'PSC_E2_{E2}')
#     secm.RUN()

