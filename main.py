# Importere library til at forbinde til adafruit.io
import umqtt_robust2
from machine import Pin, UART
import dht
from time import sleep_ms, sleep
from jarvisJokes import *
import neopixel
import sys
import GPSfunk
import KS0051Sensor
#import threading

uart1 = UART(1, baudrate=9600, tx=16, rx=17)
play = bytes([0x7E, 0xFF, 0x06, 0x0D, 0x00, 0x00, 0x01, 0xFE, 0xED, 0xEF])
pause = bytes([0x7E, 0xFF, 0x06, 0x0E, 0x00, 0x00, 0x00, 0xFE, 0xED, 0xEF])
track1 = bytes([0x7E, 0xFF, 0x06, 0x12, 0x00, 0x00, 0x01, 0xFE, 0xE8, 0xEF])
track2 = bytes([0x7E, 0xFF, 0x06, 0x12, 0x00, 0x00, 0x02, 0xFE, 0xE7, 0xEF])

n = 12
p = 15

#sætter infrared obstacle avoidence sensor til Pin 27
sensorState = 0
sensorPin = Pin(27, Pin.IN)


np = neopixel.NeoPixel(Pin(15), 12)

#from sensorListTest import *
lib = umqtt_robust2
sensor = dht.DHT11(Pin(14))
sensorList = []
#sæt TX -> pin n18

mapFeed = bytes('{:s}/feeds/{:s}'.format(b'tobi3296', b'mapfeed/csv'), 'utf-8')

speedFeed = bytes('{:s}/feeds/{:s}'.format(b'tobi3296', b'speedfeed/csv'), 'utf-8')


while True:
    sleep_ms(500)
    besked = lib.besked
    
    KS0051Sensor.IRSensor(1)
        
    # haandtere fejl i forbindelsen og hvor ofte den skal forbinde igen
    if lib.c.is_conn_issue():
        while lib.c.is_conn_issue():
            # hvis der forbindes returnere is_conn_issue metoden ingen fejlmeddelse
            lib.c.reconnect()
        else:
            lib.c.resubscribe()

    try:
                                
        lib.c.publish(topic=mapFeed, msg=GPSfunk.main())      
        speed = GPSfunk.main()        
        speed = speed[:4]       
        print("speed: ",speed)        
        lib.c.publish(topic=speedFeed, msg=speed)        
        sleep(3)
        
        
            
        if besked == "spil til 1":            
            np[0] = [255,255,0]
            np[1] = [255,255,0]
            np[2] = [255,255,0]
            np[3] = [255,255,0]
            np[4] = [255,255,0]
            np[5] = [255,255,0]
            np[6] = [255,255,0]
            np[7] = [255,255,0]
            np[8] = [255,255,0]
            np[9] = [255,255,0]
            np[10] = [255,255,0]
            np[11] = [255,255,0]
            np.write()
            print("LED'erne er taendt")
            sleep(5)
            np[0] = [0,0,0]
            np[1] = [0,0,0]
            np[2] = [0,0,0]
            np[3] = [0,0,0]
            np[4] = [0,0,0]
            np[5] = [0,0,0]
            np[6] = [0,0,0]
            np[7] = [0,0,0]
            np[8] = [0,0,0]
            np[9]= [0,0,0]
            np[10] = [0,0,0]
            np[11] = [0,0,0]
            np.write()
            print("LED'erne er slukket")
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="LED'en er taendt")
            lib.besked = ""
        
            
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        lib.client.disconnect()
        lib.sys.exit()
    except OSError as e:
        print('Failed to read sensor.')
    except TypeError as e:
        print('TypeError')
    except TypeError as e:
        print('TypeError')
    lib.c.check_msg() # needed when publish(qos=1), ping(), subscribe()
    lib.c.send_queue()  # needed when using the caching capabilities for unsent messages
lib.c.disconnect()


