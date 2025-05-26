import time
from random import random, uniform

import plasma

"""
A fire effect.
"""
rgbs = [
                (0x07,0x07,0x07),
                (0x1F,0x07,0x07),
                (0x2F,0x0F,0x07),
                (0x47,0x0F,0x07),
                (0x57,0x17,0x07),
                (0x67,0x1F,0x07),
                (0x77,0x1F,0x07),
                (0x8F,0x27,0x07),
                (0x9F,0x2F,0x07),
                (0xAF,0x3F,0x07),
                (0xBF,0x47,0x07),
                (0xC7,0x47,0x07),
                (0xDF,0x4F,0x07),
                (0xDF,0x57,0x07),
                (0xDF,0x57,0x07),
                (0xD7,0x5F,0x07),
                (0xD7,0x5F,0x07),
                (0xD7,0x67,0x0F),
                (0xCF,0x6F,0x0F),
                (0xCF,0x77,0x0F),
                (0xCF,0x7F,0x0F),
                (0xCF,0x87,0x17),
                (0xC7,0x87,0x17),
                (0xC7,0x8F,0x17),
                (0xC7,0x97,0x1F),
                (0xBF,0x9F,0x1F),
                (0xBF,0x9F,0x1F),
                (0xBF,0xA7,0x27),
                (0xBF,0xA7,0x27),
                (0xBF,0xAF,0x2F),
                (0xB7,0xAF,0x2F),
                (0xB7,0xB7,0x2F),
                (0xB7,0xB7,0x37),
                (0xCF,0xCF,0x6F),
                (0xDF,0xDF,0x9F),
                (0xEF,0xEF,0xC7),
                (0xFF,0xFF,0xFF)         
                  ]


# Set how many LEDs you have
NUM_LEDS = 64

values = [0]*64
values[0] = 40

# WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(NUM_LEDS, color_order=plasma.COLOR_ORDER_GRB)

# Start updating the LED strip
led_strip.start()

def propagate():
    #Tall fire
#     values[0] = int(uniform(35,40))
#     for i in range(NUM_LEDS-2,-1,-1):
#         values[i+1] = int(values[i] * uniform(0.9,1.0)) if random() > 0.5 else values[i]
    #Small fire
    values[0] = int(uniform(35,40))
    for i in range(NUM_LEDS-2,-1,-1):
        values[i+1] = int(values[i] * uniform(0.9999999`,1.0))


while True:
    propagate()
    # fire effect! Random red/orange hue, full saturation, random brightness
    for i in range(NUM_LEDS):
        val = rgbs[35 if values[i]>35 else values[i]]
        led_strip.set_rgb(NUM_LEDS-i,val[0],val[1],val[2])
    time.sleep(0.1)


