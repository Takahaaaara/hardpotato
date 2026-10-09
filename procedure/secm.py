import hardpotato as hp
import numpy as np
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

model = 'chi920d'
path = 'C:/Users/parasita/Downloads/chi920d/chi920d.exe'
date_str = datetime.now().strftime("%m%d%Y")
tech = 'PSC_algiment_with_SECM_pos'
folder= Path(f'data/data/{date_str}/{tech}') 
Path.mkdir(folder, parents=True, exist_ok=True)

E1 = 0.4
sesns1 = 1e-9

hp.potentiostat.Setup(model, path, str(folder))
secm = hp.potentiostat.SECM()
secm.SECM(E1=E1, sens=sesns1, xdist=300, ydist=-300, incrdist=2, incrtime=0.05, fileName='SECM_final')
secm.RUN()