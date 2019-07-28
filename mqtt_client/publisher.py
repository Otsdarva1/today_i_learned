# -*- coding:utf-8 -*-
import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect('192.168.1.102', 1883, keepalive=60)
client.publish('test/topic', 'hello world')
