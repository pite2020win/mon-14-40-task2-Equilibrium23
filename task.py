
#Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
#The program should print out current orientation, and applied tilt correction.
# (Tilt is "Roll" in this diagram https://www.novatel.com/assets/Web-Phase-2-2012/Solution-Pages/AttitudePlane.png)
#The program should run in infinite loop, until user breaks the loop. 
#Assume that plane orientation in every new simulation step is changing with random angle with gaussian distribution (the planes is experiencing "turbuence"). 
# Hint: "random.gauss(0, 2*rate_of_correction)"
#With every simulation step the orentation should be corrected, correction should be applied and printed out.
import random

def drawGround():
  for _ in range(20):
    print("*",end = '')

def drawPlaneWings(angle):
  a = 

def drawCorrection(angle):



if __name__ == "__main__":
  while True:
    tempAngle = random.gauss(0, 2*180)
    




# I have no idea what to do :(
# kind of hard to create smth impressive after 6h of classes in a row
# do anything ;) make it run     
