#ifndef MQTT_CLIENT_H
#define MQTT_CLIENT_H

#include <Arduino.h>

void setupMQTT();
void publishSensorData(String payload);
void mqttLoop();

#endif