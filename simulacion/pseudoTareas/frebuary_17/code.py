import numpy as np
import matplotlib.pyplot as plt

def get_euler(t0, tf, presente, direccion, intervalo, *args):
  futuros = []
  tiempos = []
  while(True):
    if (t0 + intervalo > tf):
      intervalo = tf - t0;
    futuros.append(presente)
    pendiente =  direccion(t0, presente, *args)
    presente = presente + pendiente *  intervalo
    t0 += intervalo
    tiempos.append(t0)
    if t0 >= tf:
      break;

  futuros = np.array(futuros)
  tiempos = np.array(tiempos)

  return futuros, tiempos



def heunz(t0, tf, presente, direccion, intervalo, *args):
  futuros = []
  tiempos = []
  while(True):
    if (t0 + intervalo > tf):
      intervalo = tf - t0;
    futuros.append(presente)
    k1 = direccion(t0, presente, *args)
    k2 = direccion((t0 + intervalo), presente + (intervalo * k1), *args)
    pendiente =  ((1.0 /  2.0)* (k1 + k2))
    presente = presente + pendiente *  intervalo
    t0 += intervalo
    tiempos.append(t0)
    if t0 >= tf:
      break;

  futuros = np.array(futuros)
  tiempos = np.array(tiempos)

  return futuros, tiempos
   

Cn = 200
k1 = 0.1
k2 = 0.1
E = 400
C0 = 150

def get_colesterol(t0, Ct, Cn, k1, E, k2): 
    dCdt = (Cn- Ct) * k1 + k2 * E
    return dCdt

colesterol, tiempo = heunz(0, 2, C0, get_colesterol, 0.1, Cn, k1, E, k2)

plt.plot(tiempo, colesterol)
plt.grid()
plt.show()

