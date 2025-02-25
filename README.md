connects a Raspberry Pi to a MySQL database, fetches relay states for specific meters, and controls relay pins based on the fetched states in a continuous loop while handling errors and cleanup.

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

#Board physical pin numbers used
#pyhsical pin declared as OUTPUT
#GPIO.LOW makes Relay ON
#GPIO.HIGH makes Relay OFF

GPIO.cleanup()           
exit()   #Exit the interpreter

sudo nano relay.py

#Code and paste, save(ctrl + X ..Y) 



			 	
               			   
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
