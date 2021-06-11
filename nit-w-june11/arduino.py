
# Read the data from Arduino
# Serial Communication

# Install a library to read the serial communication
# pip install pyserial
# pip install paho-mqtt

# Import this library
import serial
import time
import paho.mqtt.client as mqtt

# create an object to access 
# 3 Arguments - Port, Speed, timeout
ser=serial.Serial('/dev/ttyACM0',9600,timeout=0.5) # serial - module, Serial - class
print('Serial Port is Connected')

# create a client object
client=mqtt.Client() 

# Infinite Loop
while True:
 data=ser.readline()
 data=data.decode('utf-8') # bytes data into string data
 if data.startswith('#'):
  data=data.split(',')
  value1=int(data[0][1:]) # it is removing SOF (#)
  value2=int(data[1][:-3]) # ~ (EOF), \r \n
  if(value1>210 and value1<220):
   label=1
  elif(value1>220 and value1<230):
   label=2
  elif(value1>230 and value1<240):
   label=3
  elif(value1>240 and value1<250):
   label=4
  elif(value1>250 and value1<270):
   label=5
  else:
   label=6
  print(value1,value2,label)
  client.connect('52.91.45.114',1883) # broker - server - aws machine 52.91.45.114
  print('Connected with Broker')
  client.publish('nit/fdp',str(value1)+','+str(value2)+','+str(label))
 time.sleep(4)
