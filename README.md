Script for turning the relay on and off
________________________________________
connect to putty (IP Address)
clear
*************************
sudo apt update
sudo apt install python3-pip
python3 -m venv myenv
source myenv/bin/activate
pip install RPi.GPIO
pip install mysql-connector-python

copy and paste a file to another dir
________________________________________
cp /home/gonxt/Poles/relay_database.py  /home/gonxt/Poles/myenv
cd /home/gonxt/Poles/myenv/
ls -l

*************************
Python 3
import RPi.GPIO as GPIO


#Board physical pin numbers used
#pyhsical pin declared as OUTPUT
#GPIO.LOW makes Relay ON
#GPIO.HIGH makes Relay OFF

GPIO.cleanup()           
exit()   #Exit the interpreter

sudo nano relay.py

#Code and paste, save(ctrl + X ..Y) 

#********************************************************
import RPi.GPIO as GPIO
GPIO.stmode(GPIO.BCM)
import time

# Set up GPIO mode to use physical pin numbers
GPIO.setmode(GPIO.BOARD)

#GPIO  | Relay
#**************
#**************
#11     01
#12     02
#13     03
#15     04
#16     05
#18     06
#22     07
#29     08

# Define relay pins
gpioList = [5, 6]

# Set up each relay pin as an output and initialize to HIGH (off)
for i in gpioList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
	
#Sleep Time Variables
sleepTimeShort = 2.2   #Change Time
sleepTimeLong = 1.5    #Change Time

#MAIN LOOP
#*******************
try:
    # Control relays
    for i in gpioList:
        GPIO.output(i, GPIO.LOW)
        print(f"Relay connected to pin {pin} ON")
        time.sleep(sleepTimeLong);
		
        GPIO.output(i, GPIO.HIGH)

    print("Relays are all OFF")
    GPIO.cleanup()
except KeyboardInterrupt:
    print("QUIT")
    GPIO.cleanup()
#*************************************************
python relay.py

	 
_________________________________________________________________________________________________________
import Rpi.GPIO
import time
GPIO.stmode(GPIO.BCM)
	 
#GPIO  | Relay
#**************
#**************
#11     01
#12     02
#13     03
#15     04
#16     05
#18     06
#22     07
#29     08
	 
#Initiate List With Pin GPIO Pin Numbers
gpioList = [11,12,13, 15, 16, 18, 22, 29 ] #Update GPIO To what is being used
	 
for i in gpioList:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.HIGH)
		 
#Sleep Time Variables
sleepTimeShort = 2.2   #Change Time
sleepTimeLong = 1.5    #Change Time
	
#MAIN LOOP
#*******************
try:
   while True:
	  for i in gpioList:
		  GPIO.output(i, GPIO.LOW)
          time.sleep(sleepTimeShort);
		  GPIO.output(i, GPIO.HIGH)
		  time.sleep(sleepTimeShort);
#End Program Cleanly With Keyboard
except KeyboardInterrupt:
       print "Quit"	
#Reset GPIO Settings
GPIO.cleanup()
	
pyhton relay.py

*****************************************
import mysql.connector
import RPi.GPIO as GPIO
import time

# Connect to MySQL database
conn = mysql.connector.connect(
    host="13.247.23.5",
    user="robot",
    password="robot123#",
    database="polesdb"
)
cursor = conn.cursor()

# Set up GPIO mode to use physical pin N
GPIO.setmode(GPIO.BOARD)

# Define the relay pins
gpioList = [11, 12, 13, 15, 16, 18, 22, 29]

# Set up each relay pin as an output and initialize to HIGH (off)
for pin in gpioList:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def get_relay_state(meter_id):
    cursor.execute("SELECT Valid FROM relay_state WHERE Meter=%s", (meter_id,))
    result = cursor.fetchone()
    return result[0]

def set_relay(relay_pin, status):
    if status:
        print(f"Setting relay on pin {relay_pin}: ON")
        GPIO.output(relay_pin, GPIO.LOW)
    else:
        print(f"Setting relay on pin {relay_pin}: OFF")
        GPIO.output(relay_pin, GPIO.HIGH)

def update_relay_state(meter_id, status):
    cursor.execute("UPDATE relay_state SET Valid=%s WHERE Meter=%s", (status, meter_id))
    conn.commit()

# List of meters
meters = [f"0f60010001{i}" for i in range(1, 9)]

# Main loop
try:
    while True:
        for index, current_meter in enumerate(meters[:len(gpioList)]):  # Ensure the loop matches the number of relays
            valid = get_relay_state(current_meter)
            if valid == 1:
                set_relay(gpioList[index], True)  # Turn relay on
                # Check if Valid is still 1, if not set it to 1
                if get_relay_state(current_meter) != 1:
                    update_relay_state(current_meter, 1)
            else:
                set_relay(gpioList[index], False)  # Turn relay off
                # Set Valid to 0
                update_relay_state(current_meter, 0)
            time.sleep(1)  # Check the state every second
except KeyboardInterrupt:
    print("QUIT")
    GPIO.cleanup()
finally:
    GPIO.cleanup()
    cursor.close()
    conn.close()

			 	
               			   
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
