# CircuitPlaygroundExpress_Temperature
# reads the on-board temperature sensor and prints the value
 
import board 
import adafruit_thermistor
import neopixel
import time
 
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0,0,0))
pixels.show() 
thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)

def simpleCircle(wait,currenttemp):
    RED = 0x100000 # (0x10, 0, 0) also works
    YELLOW=(0x10, 0x10, 0)
    GREEN = (0, 0x10, 0)
    AQUA = (0, 0x10, 0x10)
    BLUE = (0, 0, 0x10)
    PURPLE = (0x10, 0, 0x10)
    BLACK = (0, 0, 0)

    for i in range((currenttemp/10)-1):
        pixels[i] = RED
        time.sleep(1)
        
    pixels.fill((0,0,0))
                
    for i in range((currenttemp % 10)-1):
        pixels[i] = GREEN
        time.sleep(1)
        
    pixels.fill((0,0,0))
         
 
while True:
    print("Temperature is: %f C and %f F" % (thermistor.temperature,
                                    (thermistor.temperature*9/5+32-6)))
 
    time.sleep(0.25)
    currenttemp = (thermistor.temperature*9/5+32-6)
    simpleCircle(.05,currenttemp)
