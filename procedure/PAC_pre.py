import hardpotato as hp
import numpy as np
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

model = 'chi920d'
path = 'C:/Users/parasita/Downloads/chi920d/chi920d.exe'
date_str = datetime.now().strftime("%m%d%Y")
tech = 'PAC_3'
folder= Path(f'data/data/{date_str}/{tech}')
Path.mkdir(folder, parents=True, exist_ok=True)


hp.potentiostat.Setup(model, path, str(folder))
secm = hp.potentiostat.SECM()

secm.PAC(E1=0.4, qt = 30, sens=1e-9, maxincr=0.3, iratio=45, fileName='PAC', header='PAC_pre', withdraw=150)
secm.RUN()