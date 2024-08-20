# Welcome to saellite Connector

import pgzero
from random import randint
from time import time

TITLE = "Satellite Connector"
WIDTH = 800
HEIGHT = 600

starttime = 0
endtime = 0
totaltime = 0

next_satellite = 0
number_of_satellite = 12

satellites = []

def create_satellite():
    global starttime
    for i in range(0,number_of_satellite):
        sat = Actor('sattelite')
        sat.pos = randint(50,WIDTH-50),randint(50,HEIGHT-50)
        