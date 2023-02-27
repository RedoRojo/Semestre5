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
   