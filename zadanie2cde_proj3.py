import numpy as np
import matplotlib.pyplot as plt

def population_model(a, b, c, d, e, f, initial_conditions):
    h = 0.001
    t = np.arange(0, 50, h)

    x, y = np.zeros_like(t), np.zeros_like(t)
    x[0], y[0] = initial_conditions

    for i in range(1, t.shape[0]):
        eq1 = lambda x, y: (a - b * (c * x + d * y)) * x
        eq2 = lambda x, y: (e - f * (c * x + d * y)) * y

        k1_x = h * eq1(x[i-1], y[i-1])
        k1_y = h * eq2(x[i-1], y[i-1])

        k2_x = h * eq1(x[i-1] + 0.5 * k1_x, y[i-1] + 0.5 * k1_y)
        k2_y = h * eq2(x[i-1] + 0.5 * k1_x, y[i-1] + 0.5 * k1_y)

        k3_x = h * eq1(x[i-1] + 0.5 * k2_x, y[i-1] + 0.5 * k2_y)
        k3_y = h * eq2(x[i-1] + 0.5 * k2_x, y[i-1] + 0.5 * k2_y)

        k4_x = h * eq1(x[i-1] + k3_x, y[i-1] + k3_y)
        k4_y = h * eq2(x[i-1] + k3_x, y[i-1] + k3_y)

        x[i] = x[i-1] + (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6
        y[i] = y[i-1] + (k1_y + 2*k2_y + 2*k3_y + k4_y) / 6

        x[i] = max(x[i], 0)
        y[i] = max(y[i], 0)

        if x[i] == 0 and y[i] == 0:
            break

    return x, y

a, b, c = 0.8, 1, 0.3
d, e, f = 0.4, 0.5, 0.4

initial_conditions = [(4, 8), (8, 8), (12, 8)]

fig, ax = plt.subplots()

for ic in initial_conditions:
    x, y = population_model(a, b, c, d, e, f, ic)
    ax.plot(x, y, label=f'(x, y) = {ic}')

ax.scatter(*zip(*initial_conditions), color='r', label='Warunki początkowe', marker='o')
ax.set_xlabel('Liczba osobników populacji x')
ax.set_ylabel('Liczba osobników populacji y')
ax.set_title('Portret fazowy dla różnych warunków początkowych')
ax.legend()
ax.grid(True)
plt.show()

#wszystkie w pewnym momencie dochodzą do równowagi