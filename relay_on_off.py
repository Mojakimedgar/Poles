import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)  # Suppress GPIO warnings
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering

# GPIO  | Relay
# **************
# **************
# 21     01
# 22     02
# 23     03
# 24     04
# 26     05
# 29     06
# 5      07
#3       08

# Define relay pins (only valid pins for Raspberry Pi Zero 2W)
gpioList = [21, 22, 23, 24, 26, 29,5, 3]

# Set up each relay pin as an output and initialize to HIGH (off)
for pin in gpioList:
    try:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
    except ValueError:
        print(f"Invalid pin: {pin}")

# Sleep Time Variables
sleepTimeShort = 2  # Change Time
sleepTimeLong = 10  # Change Time

# MAIN LOOP
# *******************
try:
    # Control relays
    for pin in gpioList:
        try:
            GPIO.output(pin, GPIO.LOW)
            print(f"Relay connected to pin {pin} ON")
            time.sleep(sleepTimeLong)

            GPIO.output(pin, GPIO.HIGH)
        except ValueError as e:
            print(f"Error with pin {pin}: {e}")

    print("Relays are all OFF")
    GPIO.cleanup()
except KeyboardInterrupt:
    print("QUIT")
    GPIO.cleanup()
except Exception as e:
    print(f"An error occurred: {e}")
    GPIO.cleanup()
finally:
    GPIO.cleanup()
