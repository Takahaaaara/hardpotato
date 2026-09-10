from hardpotato import potentiostat

model = 'chi920d'
path = "C:/Users/parasita/Downloads/chi920d/chi920d.exe"
folder = 'data/tests/CHI920D_test'

#print(potentiostat.models_available)
info = potentiostat.Info(model)
info.specifications()
potentiostat.Setup(model, path, folder)
umeSens = 1e-9

cv = potentiostat.CV(sr=0.5, sens=umeSens)
cv.bipot()
cv.run()

lsv = potentiostat.LSV(sr=0.5, sens=umeSens)
lsv.bipot()
lsv.run()

ca = potentiostat.CA(sens=umeSens)
ca.bipot()
ca.run()

ocp = potentiostat.OCP(sens=umeSens)
ocp.run()