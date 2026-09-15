from hardpotato import potentiostat

model = 'chi920d'
path = 'C:/Users/parasita/Downloads/chi920d/chi920d.exe'
folder = './data/tests/CV_test'

#print(potentiostat.models_available)
info = potentiostat.Info(model)
info.specifications()

Eini = 0     # V, initial potential
Ev1 = 0.8       # V, first vertex potential
Ev2 = 0      # V, second vertex potential
Efin = 0     # V, final potential
sr = 0.1        # V/s, scan rate
dE = 0.001      # V, potential increment
nSweeps = 4     # number of sweeps
sens = 1e-9     # A/V, current sensitivity
fileName = 'CV' # base file name for data file
header = 'CV'   # header for data file

potentiostat.Setup(model, path, folder)
secm = potentiostat.SECM()
secm.CV(Eini, Ev1,Ev2, Efin, sr, dE, nSweeps, sens, fileName, header)
secm.RUN()
