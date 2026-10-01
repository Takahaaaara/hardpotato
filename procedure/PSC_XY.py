import hardpotato as hp
import numpy as np
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

model = 'chi920d'
path = 'C:/Users/parasita/Downloads/chi920d/chi920d.exe'
date_str = datetime.now().strftime("%m%d%Y")
tech = 'PSC'
folder= Path(f'data/data/{date_str}/{tech}') # NOTE: verificar se isso funciona
Path.mkdir(folder, parents=True, exist_ok=True)
# folder = f'data/data/{today}'

hp.potentiostat.Setup(model, path, str(folder))
secm = hp.potentiostat.SECM()

dist = -500

secm.PSC(E1=0.4, sens=1e-9, qt=30, dir='x', dist=dist, incrdist=0.5, incrtime=0.05, fileName='PSC_X', header='PSC')
secm.RUN()
