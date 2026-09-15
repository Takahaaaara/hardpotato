from hardpotato import potentiostat

model = 'chi920d'
path = 'C:/Users/parasita/Downloads/chi920d/chi920d.exe'
folder = './data/tests/SECM_test'

print(potentiostat.models_available)
info = potentiostat.Info(model)
info.specifications()

potentiostat.Setup(model, path, folder)
secm = potentiostat.SECM()
secm.SECM(E1=0.4, qt = 30, sens=1e-8, xdist=-200, ydist=-200,
          incrtime=0.05, incrdist=5,
           fileName='SECM', header='SECM_test')
secm.RUN()