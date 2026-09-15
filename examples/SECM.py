import hardpotato as hp
import softpotato as sp

model = 'chi920d'
path = 'C:/Users/oliverrz/Desktop/CHI/chi1205b_mini2/chi1205b.exe'
folder = 'examples'

hp.potentiostat.Setup(model, path, folder)
x = 10
y = 20
secm = hp.potentiostat.SECM()
secm.PAC(E1=0.4,iratio=60, fileName='adjusting_in_z')
secm.RUN()
fileName = f'SECM_x{x}_y{y}'
secm.MOVE('step', z=-5)
secm.SECM(secmmode='i', xdist=x, ydist=y, E1=-0.1, E2=0.4, sens2=1e-9, fileName=fileName)
secm.RUN()
