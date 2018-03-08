#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

version = "v0.002"
# 08.03.2018
# At home: Github. Seperated sensehat on/off, work/home. Generation will be the same.
# Initial code at work

import importlib

# Assume SenseHat is here
sensehatpresent = 1

try:
    importlib.import_module(SenseHat)
except ImportError:
    sensehatpresent = 0
except NameError:
	print("NameError funnet, setter sensehatpresent til 0")
	sensehatpresent = 0
else:
	from sense_hat import SenseHat
	
print("Sensehatpresent is: "+str(sensehatpresent))


from random import randint
from time import sleep

# AI starter alltid i pos 0,0
# Målet er 7,7
# Det er hindringer i mellom, de kan bestå av:
# Sand: 	Gul/orange. Fart: -30%
# Fjell: 	Brun. 		Fart: -60%
# Skog: 	Mørkegrønn.	Fart: -20%
# Elv: 		Lyseblå		Fart: -10%
# Flatmark	Grønn		Fart: - 0%
# Asfalt	Grå			Fart: +10%
# Hav		Mørkeblå	Fart: -90%

if sensehatpresent == 1:
	sense = SenseHat()
	sense.low_light = False
	sense.set_rotation(180, redraw=False)

x = 0
y = 0

# Rød for AI, grønn for Mål

ai_color = 255, 0, 0
ai_x, ai_y = 0, 0

goal_color = 0, 255, 0
goal_x, goal_y = 7, 7

# Fargelegg pixler hvis sensehatpresent = 1, ellers hopp over
if sensehatpresent == 1:
	sense.set_pixel(ai_x, ai_y, (ai_color))
	sense.set_pixel(goal_x, goal_y, (goal_color))

	# Lage sti til målet med gul farge
	a = 0
	while a < 6:
		a = a + 1
		sense.set_pixel(a, a, 255, 255, 0)
		sleep(.777)

	# Lage sti med blått hav

	a = 0
	while a < 6:
		a = a + 1
		sense.set_pixel(a, a, 0, 0, 255)
		sleep(.333)
else:
	print("Sensehat finnes ikke, fargelegger ikke start, mål og sti")

types = ["sand", "fjell", "skog", "elv", "flatmark", "asfalt", "elv"]
penality = [-30, -60, -20, -10, 0, 10, -90]
farger = [[255, 165, 0],[139, 69, 19],[0, 100, 0],[0, 0, 100],[173, 255, 47],[128, 128, 128],[0,255,255]]

print("Debug, totale typer terring med attributer: ")
print(types)
print(penality)
print(farger)
# exit(1)

rtype = randint(0, 6)
print("Terrengvalg: " + str(rtype))

rterreng = types[rtype]
rpenality = penality[rtype]
# print("Debug, rpenality: "+str(rpenality))
# print("Type of rpenality: "+str(type(rpenality)))

rfarge = farger[rtype]
print("Fargevalg: " + str(rfarge))

rr = rfarge[0]
rg = rfarge[1]
rb = rfarge[2]
print("Fargevalg i RGB: " + str(rr) + " " + str(rg) + " " + str(rb))

# Prøve å lage LISTE av pixel
pixel = list()

print("type av pixel: "+str(type(pixel)))

pixel.append(rterreng)
# print("Alltid feil på rpenality...")
# print("Type: "+str(type(rpenality)))


pixel.append(str(rpenality))
pixel.append(rr)
pixel.append(rg)
pixel.append(rb)

print("Len av pixel: " + str(len(pixel)))
print("Pixel: " + str(pixel))
