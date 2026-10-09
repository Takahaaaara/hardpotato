import hardpotato as hp
import numpy as np
import matplotlib.pyplot as plt

folder = 'data/data/10072026/PSC_algiment_with_SECM'
model = 'chi920d'
            
secm = hp.load_data.SECM('SECM_final' +'.txt', folder, model)

x = secm.x
y = secm.y
z = secm.z[:, 0]
x_unique = np.unique(x)
y_unique = np.unique(y)
Z = z.reshape(len(y_unique), len(x_unique))

heatmap = plt.pcolormesh(
    x_unique,
    y_unique,
    Z,
    cmap='viridis'
)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('$X$ / µm', fontsize=18)
plt.ylabel('$Y$ / µm', fontsize=18)
plt.tight_layout()
plt.colorbar(heatmap, label='$i$ / A')
plt.show()
