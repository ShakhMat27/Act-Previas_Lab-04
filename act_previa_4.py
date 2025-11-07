# -*- coding: utf-8 -*-
"""Act_Previa_4.ipynb

Documento Original ubicado en:
    https://colab.research.google.com/drive/1rI70p1hPSrq2biDAUipukfu4I3zbk542
"""

import matplotlib.pyplot as plt
import numpy as np

#Ley de Boyle
valores= np.arange(1,6)
volumen_boyle=[3,2,1.5,1.2,1.03]
presion_boyle=[1,1.5,2,2.5,2.9]


plt.plot(volumen_boyle, presion_boyle,dash_capstyle="projecting",linewidth=2.5)
plt.plot(volumen_boyle, presion_boyle, marker="s", ls="", label="Relación Indirecta")

plt.xticks(volumen_boyle)
plt.yticks(presion_boyle)
plt.xlabel("L")
plt.ylabel("atm")
plt.title("Simulación: Ley de Boyle")
plt.legend()
plt.grid()
plt.show()

#Ley de Charles
valores= np.arange(1,6)
temperatura_charles=[298,308,318,328,338]
volumen_charles=[3,3.1,3.2,3.3,3.4]

plt.plot(temperatura_charles, volumen_charles,dash_capstyle="projecting",linewidth=2.5)
plt.plot(temperatura_charles, volumen_charles, marker="s", ls="", label="Relación Directa")

plt.xticks(temperatura_charles)
plt.yticks(volumen_charles)
plt.xlabel("K")
plt.ylabel("L")
plt.title("Simulación: Ley de Charles")
plt.legend()
plt.grid()
plt.show()

#Ley de Gay-Lussac
valores= np.arange(1,6)
temperatura_gaylussac=[298, 447, 596, 745, 864]
presion_gaylussac=[1, 1.5, 2, 2.5, 2.9]

plt.plot(temperatura_gaylussac, presion_gaylussac,dash_capstyle="projecting",linewidth=2.5)
plt.plot(temperatura_gaylussac, presion_gaylussac, marker="s", ls="", label="Relación Directa")

plt.xticks(temperatura_gaylussac)
plt.yticks(presion_gaylussac)
plt.xlabel("K")
plt.ylabel("atm")
plt.title("Simulación: Ley de Gay-Lussac")
plt.legend()
plt.grid()
plt.show()
