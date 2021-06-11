# import mqtt communication

import paho.mqtt.client as mqtt
import main

# create a client object
client=mqtt.Client()

# connect with broker
client.connect('172.31.88.64',1883)
print('Broker Connected')

# subscribe to the broker
client.subscribe('nit/ml')

# define a notifier
def notification(client,userdata,msg):
 k=(msg.payload).decode('utf-8')
 label=main.predict_output(int(k)) 
 print('The predicted output is {0}'.format(label))
 client.publish('nit/mlr',str(label[0]))


# configure the notifier
client.on_message=notification
client.loop_forever()
