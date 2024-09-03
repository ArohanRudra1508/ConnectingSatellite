# Welcome to Satellite Connector

import pgzrun
from random import randint
from time import time

TITLE = "Satellite Connector"
WIDTH = 800
HEIGHT = 600

starttime = 0
endtime = 0
total_time = 0

next_satellite = 0
number_of_satellite = 12

satellites = []
lines = []

def create_satellite():
    global starttime
    for i in range(0,number_of_satellite):
        sat = Actor('sattelite')
        sat.pos = randint(50,WIDTH-50),randint(50,HEIGHT-50)
        # Part 2
        satellites.append(sat)
    starttime = time()

def draw():
    global total_time
    screen.blit('satbg',(0,0))
    n = 1
    for sat in satellites:
        screen.draw.text(str(n),(sat.pos[0],sat.pos[1]+20),fontsize = 20)
        sat.draw()
        n+=1
    
    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))
    if next_satellite < number_of_satellite:
        total_time = time() - starttime
        screen.draw.text(str(round(total_time,2)),(350,450),fontsize = 20)
    else:
        screen.draw.text(str(round(total_time,2)),(350,450),fontsize = 20)
# Part 3
def on_mouse_down(pos):
    global next_satellite, lines
    if next_satellite <  number_of_satellite:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite -1].pos,satellites[next_satellite].pos))
        else:
            next_satellite = 0
            lines = 0

create_satellite()

    
pgzrun.go()
