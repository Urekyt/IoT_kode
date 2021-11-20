from machine import Pin
from time import sleep

sensorState = 0

sensorPin = Pin(27, Pin.IN)

while True:
    sensorState = sensorPin.value()
    sleep(0.1)
    
    if sensorState >= 1:
        print("no activity")
        print(sensorState)
        
    else:
        print("activity")
        print(sensorState)
