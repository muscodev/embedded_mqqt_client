#include "mqqt_client.h"
#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include "config.h"
#include <Arduino.h>

WiFiClientSecure espClient;
PubSubClient client = PubSubClient(espClient);

void setupMQTT() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.println("WiFi conneting ");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");
  Serial.println(WiFi.localIP());
  espClient.setInsecure();
  Serial.println(MQTT_HOST);
  Serial.println(MQTT_PORT);
  client.setServer(MQTT_HOST,MQTT_PORT);
}
void publishSensorData(String payload){
  
  if(!client.connected()){
    Serial.println("Mqtt conecting ..");
    if(client.connect("Railway",MQTT_USER,MQTT_PASS)){
      Serial.println("Mqtt clent connected");
    }
    else{
      Serial.print("failed, rc=");
      Serial.println(client.state());
    };

  }
  client.publish(MQTT_TOPIC, payload.c_str());

}
void mqttLoop() {
    client.loop();
}
