import numpy as np
t0 =0
t1 = 20
dt = 0.1

tijd = np.linspace(t0, t1, 1 + round((t1 - 10) / dt))
print(len(tijd))