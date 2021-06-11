
# import mqtt for communication

import paho.mqtt.client as mqtt

# create a client object
client=mqtt.Client()

# connect with broker
client.connect('52.91.45.114',1883)
print('Connected with Broker')

client.subscribe('nit/mlr') # read data from ml - result

# notifier
def notification(client,userdata,msg):
 print(msg.payload)

# configure this notifier
client.on_message=notification
client.loop_forever()
