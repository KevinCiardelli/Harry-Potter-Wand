
import board
import time
import digitalio
import busio
import neopixel
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_bluefruit_connect.packet import Packet


from adafruit_led_animation.color import (
    AMBER, #(255, 100, 0)
    AQUA, # (50, 255, 255)
    BLACK, #OFF (0, 0, 0)
    BLUE, # (0, 0, 255)
    CYAN, # (0, 255, 255)
    GOLD, # (255, 222, 30)
    GREEN, # (0, 255, 0)
    JADE, # (0, 255, 40)
    MAGENTA, #(255, 0, 20)
    OLD_LACE, # (253, 245, 230)
    ORANGE, # (255, 40, 0)
    PINK, # (242, 90, 255)
    PURPLE, # (180, 0, 255)
    RED, # (255, 0, 0)
    TEAL, # (0, 255, 120)
    WHITE, # (255, 255, 255)
    YELLOW, # (255, 150, 0)
    RAINBOW # a list of colors to cycle through
##     RAINBOW is RED, ORANGE, YELLOW, GREEN, BLUE, and PURPLE ((255, 0, 0), (255, 40, 0), (255, 150, 0), (0, 255, 0), (0, 0, 255), (180, 0, 255))
)

colors = [RED, MAGENTA, AQUA, TEAL, GREEN]

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.5, auto_write = True
strip = neopixel.NeoPixel(board.A1, 30, brightness = 0.5, auto_write = True)

while True:
    ble.start_advertising(advertisement)
    print("Waiting to connect")

    while not ble.connected:
        pixels.fill(YELLOW)
        pass

    print("Connected")
    pixels.fill(PURPLE)
    while ble.connected:
        s = uart.readline()
        if len(s) == 5:
            strip.fill((255,255,255))
            
