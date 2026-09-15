from hardpotato import potentiostat

model = 'chi920d'
path = 'C:/Users/parasita/Downloads/chi920d/chi920d.exe'
folder = 'data/tests/PSC_test'

print(potentiostat.models_available)
info = potentiostat.Info(model)
info.specifications()

potentiostat.Setup(model, path, folder)
secm = potentiostat.SECM()
secm.PAC(E1=0.4, qt = 30, sens=1e-8, maxincr=0.5, iratio=80, fileName='PAC', header='PAC_test', withdraw=100)
secm.RUN()
E2List = [0, 0.4, -0.4]
for E2 in E2List:
    secm.MOVE('step', z=-150)
    secm.PSC(E1=0.4, dist=150, qt=30, E2=E2, sens2=1e-4,sens=1e-8, fileName=f'PSC_E2_{E2}', header=f'PSC_E2_{E2}')
    secm.RUN()

