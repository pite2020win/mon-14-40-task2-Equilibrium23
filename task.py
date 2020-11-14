from abc import ABC,abstractmethod
import threading

class AngleEvent(ABC):
  def __init__(self,angle):
    self.angle = angle

  @abstractmethod      
  def apply_angle_changes(self,change_angle):
      pass

class Correction(AngleEvent):
  def __init__(self,angle):
    super().__init__(angle)

  def apply_angle_changes(self, change_angle):
      self.angle -= change_angle
      return self.angle

class Turbulence(AngleEvent):
  def __init__(self,angle):
        super().__init__(angle)

  def apply_angle_changes(self, change_angle):
      self.angle += change_angle
      return self.angle

from random import gauss

def angle_generator():
  while True:
    yield gauss(0,180)

class Plane:
  def __init__(self, name,angle):
    self.name = name
    self.angle = angle
    self.turbulance_angle = 0
    self.turbulence = Turbulence(angle)
    self.correction = Correction(angle)
    self.angle_gen = angle_generator()


  def storm(self):
    self.turbulance_angle = next(self.angle_gen)
    self.angle = self.turbulence.apply_angle_changes( self.turbulance_angle )
    self.correction.angle = self.angle
    

  def auto_pilot(self):
    self.angle = self.correction.apply_angle_changes( self.turbulance_angle )
    self.turbulence.angle = self.angle
        

from time import sleep
from sys import exit


if __name__ == '__main__':
    
  plane1 = Plane("Boeing",0)
  plane2 = Plane("Airbus",0)

  info = {plane1.name:plane1.angle,plane2.name:plane2.angle}

  while True:
    print("Storm is comming:")

    plane1.storm()
    info[plane1.name] = plane1.angle

    plane2.storm()
    info[plane2.name] = plane2.angle

    print(info)
    if abs(plane1.angle - plane2.angle) < 1:
      print("Planes {} and {} just crashed".format(plane1.name,plane2.name)) 
      exit()  

    print("Auto Pilot correction:")

    plane1.auto_pilot()
    info[plane1.name] = plane1.angle

    plane2.auto_pilot()
    info[plane2.name] = plane2.angle

    print(info)
    sleep(0.5)