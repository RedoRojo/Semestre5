import funciones
import matplotlib.pyplot as plt
import numpy as np

def get_conscientes(t, c, p, k): 
    dCdt = k * (p-c)
    return dCdt

cant, tiempos = funciones.heunz(0, 10, 0, get_conscientes, 0.1, 1000000, 0.5)

#plt.plot(tiempos, cant)
plt.grid()

def get_temperatura(t, T, tA, k): 
    dTdt = k * (T- tA)
    return dTdt

temps, ts = funciones.heunz(0, 200, 47, get_temperatura, 0.1, 2, -0.10116)

plt.plot(ts, temps)
plt.xlabel("tiempo")
plt.ylabel("temperatura")

plt.show()


