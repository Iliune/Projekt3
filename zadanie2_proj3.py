import numpy as np
import matplotlib.pyplot as plt

def oblicz_nastepna_populacje(a, b, c, d, aktualne_a, aktualne_b):
    da_dt = (a - b * (c * aktualne_a + d * aktualne_b)) * aktualne_a
    db_dt = (a - b * (c * aktualne_a + d * aktualne_b)) * aktualne_b

    k1_a = h * da_dt
    k1_b = h * db_dt

    k2_a = h * ((a - b * (c * (aktualne_a + 0.5 * k1_a) + d * (aktualne_b + 0.5 * k1_b))) * (aktualne_a + 0.5 * k1_a))
    k2_b = h * ((a - b * (c * (aktualne_a + 0.5 * k1_a) + d * (aktualne_b + 0.5 * k1_b))) * (aktualne_b + 0.5 * k1_b))

    k3_a = h * ((a - b * (c * (aktualne_a + 0.5 * k2_a) + d * (aktualne_b + 0.5 * k2_b))) * (aktualne_a + 0.5 * k2_a))
    k3_b = h * ((a - b * (c * (aktualne_a + 0.5 * k2_a) + d * (aktualne_b + 0.5 * k2_b))) * (aktualne_b + 0.5 * k2_b))

    k4_a = h * ((a - b * (c * (aktualne_a + k3_a) + d * (aktualne_b + k3_b))) * (aktualne_a + k3_a))
    k4_b = h * ((a - b * (c * (aktualne_a + k3_a) + d * (aktualne_b + k3_b))) * (aktualne_b + k3_b))

    nastepna_a = aktualne_a + (k1_a + 2 * k2_a + 2 * k3_a + k4_a) / 6
    nastepna_b = aktualne_b + (k1_b + 2 * k2_b + 2 * k3_b + k4_b) / 6

    return max(nastepna_a, 0), max(nastepna_b, 0)

a1, b1, c1, d1 = 1.25, 0.5, 0.1, 0.0
a2, b2, c2, d2 = 0.5, 0.2, 0.2, 0.0

h = 0.01
punkty_czasu = np.arange(0, 50, h)

poczatkowe_a, poczatkowe_b = 3, 4
populacje_a = [poczatkowe_a]
populacje_b = [poczatkowe_b]

for i in range(1, punkty_czasu.shape[0]):
    poczatkowe_a, poczatkowe_b = oblicz_nastepna_populacje(a1, b1, c1, d1, poczatkowe_a, poczatkowe_b)
    populacje_a.append(poczatkowe_a)
    populacje_b.append(poczatkowe_b)

    if poczatkowe_a == 0 and poczatkowe_b == 0:
        break

fig, osie = plt.subplots()
osie.plot(punkty_czasu, populacje_a, color='purple', label='Populacja 1')
osie.plot(punkty_czasu, populacje_b, color='orange', label='Populacja 2')
osie.set_xlabel('Czas')
osie.set_ylabel('Liczba osobników')
osie.legend()
plt.show()


#po czasie dochodzi do stanu równowagi
