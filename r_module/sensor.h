#ifndef sensor_H
#define sensor_H
#include <Arduino.h>



#define DIGITAL_SENSOR_COUNT  5

extern int sensors[DIGITAL_SENSOR_COUNT];
void InitSensors();
String SensorsToJson();

#endif