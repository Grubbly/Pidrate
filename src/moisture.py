import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

moisture_pin = 14

GPIO.setup(moisture_pin, GPIO.IN)

def readMoisture():
    print(GPIO.input(moisture_pin))

if __name__ == "__main__":
    print("Starting moisture sensing")
    while True:
        readMoisture()
        time.sleep(0.2)