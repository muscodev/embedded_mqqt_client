import dotenv
import os


dotenv.load_dotenv()

HIVEMQ_HOST = os.getenv("hivemq_host")
HIVEMQ_PORT = int(os.getenv("hivemq_port"))
MQTT_TOPIC = os.getenv("mqtt_topic")
HIVEMQ_USERNAME = os.getenv("hivemq_username")
HIVEMQ_PASSWORD = os.getenv("hivemq_password")
