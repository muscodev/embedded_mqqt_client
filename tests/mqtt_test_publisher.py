import time
import logging
import paho.mqtt.client as mqtt
import config


logging.basicConfig(level=logging.DEBUG)


def on_connect(mqttc, obj, flags, reason_code, properties):
    print("reason_code: " + str(reason_code))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid, reason_code, properties):
    print("mid: " + str(mid))


def on_log(mqttc, obj, level, string):
    print(string)


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)
client.enable_logger()
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.username_pw_set(config.HIVEMQ_USERNAME, config.HIVEMQ_PASSWORD)
client.connect(config.HIVEMQ_HOST, config.HIVEMQ_PORT, 60)
client.loop_start()
time.sleep(1)
client.publish(config.MQTT_TOPIC, payload="This is Test before mqtt from esp8266", qos=1)

time.sleep(1)
client.disconnect()
