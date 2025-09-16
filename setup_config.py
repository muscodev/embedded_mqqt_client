import dotenv
import os

dotenv.load_dotenv()


with open("r_module/config.cpp", "w") as f:
    f.write(f"""
#include "config.h"
// WiFi configuration
const char* WIFI_SSID = "{os.getenv("wifi_ssid")}";
const char* WIFI_PASSWORD = "{os.getenv("wifi_password")}";
const char* MQTT_HOST = "{os.getenv("mqtt_host")}";
const int MQTT_PORT = {os.getenv("mqtt_port")};
const char* MQTT_USER = "{os.getenv("mqtt_user")}";
const char* MQTT_PASS = "{os.getenv("mqtt_pass")}";
const char* MQTT_TOPIC = "{os.getenv("mqtt_topic")}";
const char* MODULE_ID = "{os.getenv("module_id")}";
    """)
print("Configuration file 'r_module/config.cpp' generated successfully.")