#include "config.h"
#include <ESP8266WiFi.h>
#include "mqqt_client.h"
#include "sensor.h"

void setup() {
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  InitSensors();
  setupMQTT();

}

void loop() {
  mqttLoop();
  // Set pin HIGH
  digitalWrite(2,HIGH);
  delay(100);
  publishSensorData(SensorsToJson());
  // Set pin LOW
  digitalWrite(2,LOW);
  delay(100);
}
