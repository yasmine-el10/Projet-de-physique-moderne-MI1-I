from numpy import pi, exp, sqrt, real, imag, zeros, linspace
# on importe les fonctions numpy dont on va avoir besoin

import matplotlib.pyplot as plt
# pour faire le graphique

def PlaneWave(amp, k, omega, x, t):
    return amp * exp(1j * (k * x - omega * t))
# fonction qui calcule l'onde plane Ψ(x,t) = A*e^(i(kx-ωt))

amp = 1
k = 1
omega = 1
t = 0
# on fixe l'amplitude, le nombre d'onde, la pulsation, et on regarde à t=0

lam = 2 * pi / k
# longueur d'onde associée à k

x = linspace(-3 * lam, 3 * lam, 300)
# 300 points entre -3λ et +3λ, pour voir plusieurs oscillations

psi = PlaneWave(amp, k, omega, x, t)
# on calcule l'onde pour tous les points x

fig, ax = plt.subplots()
# on crée la figure et les axes

ax.plot(x, real(psi), label="Re[Ψ(x,t)]")
ax.plot(x, imag(psi), label="Im[Ψ(x,t)]")
# on trace la partie réelle et la partie imaginaire de Ψ

ax.set_title("Onde plane à 1D")
ax.set_xlabel("x")
ax.set_ylabel("Ψ(x,t)")
ax.legend()
# titre, noms des axes, légende

plt.show()
# affichage du graphique
