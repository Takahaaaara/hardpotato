from hardpotato import potentiostat
from datetime import datetime
from pathlib import Path

model = 'chi920d'
path = 'C:/Users/parasita/Downloads/chi920d/chi920d.exe'
date_str = datetime.now().strftime("%m%d%Y")
tech = 'cv_glass'
folder= Path(f'data/data/{date_str}/{tech}') 
Path.mkdir(folder, parents=True, exist_ok=True)

#print(potentiostat.models_available)
info = potentiostat.Info(model)
info.specifications()

Eini = 0     # V, initial potential
Ev1 = -0.2       # V, first vertex potential
Ev2 = 0.4      # V, second vertex potential
Efin = 0.4     # V, final potential
sr = 0.1        # V/s, scan rate
dE = 0.001      # V, potential increment
nSweeps = 4     # number of sweeps
sens = 1e-8     # A/V, current sensitivity
fileName = '10012026_UME5_Pre_CV_FcMeOH1mM' # base file name for data file
header = 'CV'   # header for data file

potentiostat.Setup(model, path, str(folder))
secm = potentiostat.SECM()


secm.CV(Eini, Ev1,Ev2, Efin, sr, dE, nSweeps, sens, fileName, header)
secm.RUN()