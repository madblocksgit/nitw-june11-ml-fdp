# import the module
import paho.mqtt.client as mqtt
from pymongo import MongoClient

# create a client to acess db
dbclient=MongoClient('127.0.0.1',27017)
db=dbclient['nitfdp']
c=db['finaldata']

# create a client
client=mqtt.Client() # Client() - class

# connect with broker
client.connect('172.31.88.64',1883)
print('Connected with Broker')

# subscribe on a topic with broker
client.subscribe('nit/fdp')

# define a function to notify whenever sub gets a message
def notification(client,userdata,msg):
 k=(msg.payload).decode('utf-8')
 k=k.split(',')
 value1=int(k[0])
 value2=int(k[1])
 label=int(k[2])
 a={}
 a['mq3']=value1
 a['mq2']=value2
 a['label']=label
 c.insert_one(a)
 print('Data Inserted - {0} {1} {2}'.format(value1,value2,label))


# call this notification automatically
client.on_message=notification

# call this loop forever
client.loop_forever()
