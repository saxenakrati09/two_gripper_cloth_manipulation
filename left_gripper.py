import bge, time
from mathutils import Vector
import os
import csv

controller = bge.logic.getCurrentController()
#controller.activate("left_Motion")
obj = controller.owner

t = time.time()
v = Vector(obj.worldLinearVelocity)
m = obj.mass

def main():
    global t, v, m

    csvfile1 = "\forceapplied\\clothleft1.csv"
    force = [0.0,0.0,-0.0001]
    obj.applyForce(force)


    #compute change in time
    
    
    dt = time.time() - t
    t += dt

    #calculate change in velocity
    dv = Vector(obj.worldLinearVelocity) - v
    v += dv

    #force is change in momentum, which is velocity times mass, divided by time
    f = m * dv / dt
    mylist= [f[-1],dv[-1],dt]
    with open(csvfile1, "a") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows([mylist])   
    print([mylist])
    
    #!!!!!!!!!!!!!!!!
    #CAUTION
    #PLEASE DELETE THE FILE ALREADY PRESENT IN THE FOLDER
    #OTHERWISE IT APPENDS
    #OR KEEP CHANGING THE FILENAME WHEN SAVING DATA AGAIN AND AGAIN
    #!!!!!!!!!!!!!!!!!!!!!!!!
