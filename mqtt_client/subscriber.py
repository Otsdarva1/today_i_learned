# -*- coding:utf-8 -*-
import paho.mqtt.client as mqtt
def on_connect(client, userdata, flags, respons_code):
    topic = 'test/topic'
    print('watch %s' % topic)
    client.subscribe(topic)
def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('192.168.1.102', 1883, keepalive=60)
client.loop_forever()