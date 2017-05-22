#!/usr/bin/env python

from scipy.stats import norm
from scipy.stats import tmean
from scipy.stats import tstd
import random

MU = 15000
SIGMA = 4500
COSTO_MAX_PARTES = 1000
COSTO_MIN_PARTES = 800

def demanda():
	return norm.ppf(random.random() , MU, SIGMA)

def costoPartes():
	return (COSTO_MAX_PARTES - COSTO_MIN_PARTES)*random.random() + COSTO_MIN_PARTES

def manoObra():
	rnd = random.random()
	if 0 <= rnd < 0.1:
		return 430
	elif 0.1 <= rnd < 0.3:
		return 440 
	elif 0.3 <= rnd < 0.7:
		return 450
	elif 0.7 <= rnd < 0.9:
		return 460
	elif 0.9 <= rnd < 1:
		return 470

def utilidad (c1, c2, x):
	return (2490 - c1 - c2)*x - 10000000

def main():

	numSimulaciones = 100000
	matrizResultados = []
	for i in range(numSimulaciones):
		nuevaSim = [manoObra(), costoPartes(), demanda()]
		nuevaSim.append(utilidad(nuevaSim[0], nuevaSim[1], nuevaSim[2]))
		matrizResultados.append(nuevaSim)

	matrizResultados.sort(key=lambda x: x[3])

	total = 0
	numSimPerdidas = 0
	for ren in matrizResultados:
		total += ren[3]
		if ren[3] < 0:
			numSimPerdidas += 1

	print(matrizResultados[0])
	print(matrizResultados[numSimulaciones-1])

	print(total/numSimulaciones)
	
	print(numSimPerdidas/float(numSimulaciones) * 100)

if __name__ == '__main__':
	main()