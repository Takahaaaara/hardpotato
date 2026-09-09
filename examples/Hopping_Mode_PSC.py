import hardpotato as hp
import softpotato as sp
import numpy as np

model = 'chi920d'
path = 'C:/Users/oliverrz/Desktop/CHI/chi1205b_mini2/chi1205b.exe'
folder = 'C:/Users/oliverrz/Desktop/data'

hp.potentiostat.Setup(model, path, folder)

secm = hp.potentiostat.SECM()
stepx = 1
stepy = 5
i = []
for x in range (0,3,stepx):
    for y in range (0, 15, stepy):
        fileName = f'PAC_x{x}_y{y}'
        secm.MOVE('step', x=stepx, z=-150)
        secm.PAC(E2=-0.4, sens2=0.3, resistance=100, fileName=pacFileName)
        secm.RUN()

        data = hp.load_data.PAC(fileName + '.txt', folder, model)
        i.append(data.i)
i = np.array(i)
d = data.d

sp.plotting.plot(d, i, xlab='$d$ / um',fig=1,show=1)