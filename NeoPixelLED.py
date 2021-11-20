from machine import Pin, I2C
import neopixel
from lysSensor import *
#from time import sleep_ms
i2c = I2C(0, scl = Pin(22),sda = Pin(21), freq = 100000)

if i2c.scan() != []:
    sensor = TCS34725(i2c)
    sensor.gain(60)
    data = sensor.read(True)
    print(html_rgb(data))

n = 12
p = 15

np = neopixel.NeoPixel(Pin(15), 12)


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

