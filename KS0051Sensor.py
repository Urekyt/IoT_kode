from machine import Pin, UART
from time import sleep

uart1 = UART(1, baudrate=9600, tx=16, rx=17)
play = bytes([0x7E, 0xFF, 0x06, 0x0D, 0x00, 0x00, 0x01, 0xFE, 0xED, 0xEF])
pause = bytes([0x7E, 0xFF, 0x06, 0x0E, 0x00, 0x00, 0x00, 0xFE, 0xED, 0xEF])
track1 = bytes([0x7E, 0xFF, 0x06, 0x12, 0x00, 0x00, 0x01, 0xFE, 0xE8, 0xEF])

sensorState = 0
sensorPin = Pin(27, Pin.IN)

def IRSensor(timeSleep):
    
    #while True:
    sensorState = sensorPin.value()
        
    if sensorState < 1:        
        print("activity")
        uart1.write(track1)
        print(sensorState)
        uart1.write(play)
        sleep(timeSleep)
        
    else:
        print("no activity")
        print(sensorState) 
        uart1.write(pause)