import dotenv
import os


dotenv.load_dotenv()

HIVEMQ_HOST = os.getenv("mqtt_host")
HIVEMQ_PORT = int(os.getenv("mqtt_port"))
MQTT_TOPIC = os.getenv("mqtt_topic")
HIVEMQ_USERNAME = os.getenv("mqtt_user")
HIVEMQ_PASSWORD = os.getenv("mqtt_pass")
