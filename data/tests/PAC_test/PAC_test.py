from hardpotato import potentiostat

model = 'chi920d'
path = 'C:/Users/parasita/Downloads/chi920d/chi920d.exe'
folder = './data/tests/PAC_test'

#print(potentiostat.models_available)
info = potentiostat.Info(model)
info.specifications()

potentiostat.Setup(model, path, folder)
secm = potentiostat.SECM()
secm.MOVE('step', y=-1000, z=-150)
secm.PAC(E1=0.4, qt = 30, sens=1e-8, maxincr=0.5, iratio=80, fileName='PAC_y0', header='PAC_test')
secm.RUN()
secm.MOVE('step', y=1000, z=-150)
secm.PAC(E1=0.4, qt = 30, sens=1e-9, maxincr=0.5, iratio=80, fileName='PAC_yminus1000', header='PAC_test_2')
secm.RUN()

