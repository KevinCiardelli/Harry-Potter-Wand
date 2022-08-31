# Harry-Potter-Wand
from adafruit_ble import BLERadio
import time
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
import speech_recognition as sr
import board
import neopixel
import pygame

path = "/home/pi/12_drum_sounds/"
sound_files=["bass_hit_c.wav","bd_tek.wav","bd_zome.wav","bubbles.wav","clap.wav","drum_cowbell.wav","elec_cymbal.wav","elec_hi_snare.wav","pierce.wav","scratch.wav","soft_bass.wav","tap_tap_slap.wav","two_crickets.wav","lumos.wav"]
pygame.mixer.init()
speaker_volume=0.75
pygame.mixer.music.set_volume(speaker_volume)


ble = BLERadio()

uart_connection = None
tester=0
send1= "Lumos"
send2= "Aguamenti"



def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""


while True:
    if not uart_connection:
        print("Trying to connect...")

        for adv in ble.start_scan(ProvideServicesAdvertisement):
            if UARTService in adv.services:
                uart_connection = ble.connect(adv)
                uart_service = uart_connection[UARTService]
                print("Connected")
                tester=1;
                break
        ble.stop_scan()

    if(tester==1):
        word=main()
        if(word=="Lumos"):
            uart_service.write(send1.encode("utf-8"))
            for sound_file in sound_files:
            if(sound_file=="lumos.wav"):
                pygame.mixer.music.load(path+sound_file)
                print("played")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy()== True:
                    continue
            print("Lumos")
        elif(word=="Aguamenti"):
            uart_service.write(send2.encode("utf-8"))
            for sound_file in sound_files:
            if(sound_file=="bubbles.wav"):
                pygame.mixer.music.load(path+sound_file)
                print("played")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy()== True:
                    continue
            print("Aguamenti")
