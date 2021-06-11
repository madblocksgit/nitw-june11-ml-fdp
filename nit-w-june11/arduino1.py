
# import the serial for reading the data

import serial

# import mqtt communication
import paho.mqtt.client as mqtt

# create a client object
client=mqtt.Client()

# create a serial object
ser=serial.Serial('/dev/ttyACM0',9600,timeout=0.5)

# Infinite Loop
while True:
 data=ser.readline()
 data=data.decode('utf-8')
 if(data.startswith('#')):
  data=data.split(',')
  value1=data[0][1:]
  print(value1)
  client.connect('52.91.45.114',1883)
  print('Connected with Broker')
  client.publish('nit/ml',value1)
