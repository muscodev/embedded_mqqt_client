#include <Arduino.h>
#include "sensor.h"
#include "config.h"
#include <ArduinoJson.h>
// D Label	GPIO Number
// D0	GPIO16
// D1	GPIO5
// D2	GPIO4
// D3	GPIO0
// D4	GPIO2
// D5	GPIO14
// D6	GPIO12
// D7	GPIO13
// D8	GPIO15
int sensors[DIGITAL_SENSOR_COUNT] = {5,4,0,14,12};

void InitSensors(){
    for(int i = 0 ;i< DIGITAL_SENSOR_COUNT; i++)
    {
        pinMode(sensors[i], INPUT_PULLUP);
    }
}

String SensorsToJson(){

  JsonDocument doc;
  doc["ID"] = MODULE_ID;
  for(int i = 0; i< DIGITAL_SENSOR_COUNT; i++ )
  {
      doc[String(sensors[i])] = String(digitalRead(sensors[i]));
  }
  String output;
  serializeJson(doc,output);
  serializeJson(doc,Serial);
  Serial.println();
  return output;
}