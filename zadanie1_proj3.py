import numpy as np
import matplotlib.pyplot as plt

K = 100000
a, b, c = 75, 10, 0.4
d = c

dt = 0.1
t_m = 150

t_v = [a]
x_g = [b]
x_v = [b]

for t in np.arange(a, t_m, dt):
    dx_g = c * x_g[-1] * np.log(K / x_g[-1])
    x_g.append(x_g[-1] + dx_g * dt)
    
    dx_v = d * x_v[-1] * (1 - x_v[-1] / K)
    x_v.append(x_v[-1] + dx_v * dt)
    
    t_v.append(t + dt)

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))

axes.plot(t_v, x_g, label='Gompertz Model', linestyle='-', color='#FFB6C1')
axes.plot(t_v, x_v, label='Verhulst Model', linestyle='--', color='#FF1493')

axes.set_xlabel('Czas')
axes.set_ylabel('Rozmiar')

axes.legend()
plt.show()
