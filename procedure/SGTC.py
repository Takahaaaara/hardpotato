import hardpotato as hp
import numpy as np
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

model = 'chi920d'
path = 'C:/Users/parasita/Downloads/chi920d/chi920d.exe'
date_str = datetime.now().strftime("%m%d%Y")
tech = 'SGTC'
folder= Path(f'data/data/{date_str}/{tech}')
Path.mkdir(folder, parents=True, exist_ok=True)


hp.potentiostat.Setup(model, path, str(folder))
secm = hp.potentiostat.SECM()

secm.CV(E1=)
secm.RUN()