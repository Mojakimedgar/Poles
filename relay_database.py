import mysql.connector
import RPi.GPIO as GPIO
import time

# Attempt to connect to MySQL database
try:
    conn = mysql.connector.connect(
        host="13.247.23.5",
        user="robot",
        password="robot123#",
        database="polesdb"
    )
    cursor = conn.cursor()
    db_connected = True
except mysql.connector.Error as err:
    print(f"Error: {err}")
    db_connected = False

# Set up GPIO mode to use physical pin numbering
GPIO.setwarnings(False)  # Suppress GPIO warnings
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering

# Define relay pins (only valid pins for Raspberry Pi Zero 2W)
gpioList = [21, 22, 23, 24, 26, 29, 5, 3]

# Set up each relay pin as an output and initialize to HIGH (off)
for pin in gpioList:
    try:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
    except ValueError:
        print(f"Invalid pin: {pin}")

def get_relay_state(meter_id):
    if db_connected:
        try:
            cursor.execute("SELECT Valid FROM relay_state WHERE Meter=%s", (meter_id,))
            result = cursor.fetchone()
            if result:
                print(f"Fetched Valid={result[0]} for Meter={meter_id}")
                return result[0]
            else:
                print(f"No record found for Meter={meter_id}")
                return 0
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            return 0
    else:
        return 0

def set_relay(relay_pin, status):
    if status:
        print(f"Setting relay on pin {relay_pin}: ON")
        GPIO.output(relay_pin, GPIO.LOW)
    else:
        print(f"Setting relay on pin {relay_pin}: OFF")
        GPIO.output(relay_pin, GPIO.HIGH)

def update_relay_state(meter_id, status):
    if db_connected:
        try:
            cursor.execute("UPDATE relay_state SET Valid=%s WHERE Meter=%s", (status, meter_id))
            conn.commit()
            print(f"Updated Valid={status} for Meter={meter_id}")
        except mysql.connector.Error as err:
            print(f"Database error: {err}")

# List of meters
meters = [f"0f6001000{i}" for i in range(1, 9)]

# Sleep Time Variables
sleepTimeShort = 2  # Change Time
sleepTimeLong = 2  # Change Time

# Main loop
try:
    while True:
        for index, current_meter in enumerate(meters[:len(gpioList)]):  # Ensure the loop matches the number of relays
            valid = get_relay_state(current_meter)
            print(f"Meter: {current_meter}, Valid: {valid}")  # Debugging
            if valid == 1:
                set_relay(gpioList[index], True)  # Turn relay on
                # Check if Valid is still 1, if not set it to 1
                if get_relay_state(current_meter) != 1:
                    update_relay_state(current_meter, 1)
            else:
                set_relay(gpioList[index], False)  # Turn relay off
                # Set Valid to 0
                update_relay_state(current_meter, 0)
            time.sleep(sleepTimeLong)  # Sleep for the long duration

    print("Relays are all OFF")
    GPIO.cleanup()
except KeyboardInterrupt:
    print("QUIT")
    GPIO.cleanup()
except Exception as e:
    print(f"An error occurred: {e}")
    GPIO.cleanup()
finally:
    if db_connected:
        cursor.close()
        conn.close()
    GPIO.cleanup()
