import numpy as np
import matplotlib.pyplot as plt
import math
diff = 5
c1 = 1
c2 = 2
c3 = 3
sig = math.sqrt(1)
x1 = np.linspace(c1 - diff, c1 + diff, 500)
x2 = np.linspace(c2 - diff, c2 + diff, 500)
x3 = np.linspace(c3 - diff, c3 + diff, 500)
y1 = np.exp(-(x1 - c1) ** 2 / (2 * sig ** 2))
y2 = np.exp(-(x2 - c2) ** 2 / (2 * sig ** 2))
y3 = np.exp(-(x3 - c3) ** 2 / (2 * sig ** 2))
plt.plot(x1, y1, "r-", linewidth=2)
plt.plot(x2, y2, "g-", linewidth=2)
plt.plot(x3, y3, "b-", linewidth=2)
plt.grid(True)
plt.show()