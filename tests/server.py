import asyncio
from aiohttp import web
from pathlib import Path
from mqtt_test_consumer import client, mqtt
import sensor_map
import threading
import json

test_dir = Path(__file__).parent


async def index(request):
    with open(test_dir / "index.html", "r") as f:
        html_content = f.read()
        return web.Response(text=html_content, content_type='text/html')

WS = {'soket': None}


async def wshandle(request):
    global WS
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    WS['soket'] = ws
    while True:
        await asyncio.sleep(1)

    return ws


async def send_message(message: dict = None):
    ws: web.WebSocketResponse = WS['soket']
    if ws is not None and message is not None:
        await ws.send_json(message)

def consume(mqttc, obj, msg: mqtt.MQTTMessage):
    try:
        load = json.loads(msg.payload.decode())
        sensor = sensor_map.mappintoSensor(load)
        asyncio.run(send_message(sensor))
    except Exception as e:
        print("Error processing message:", e)


client.on_message = consume

app = web.Application()
app.router.add_get('/', index)
app.router.add_get('/ws', wshandle)

threading.Thread(target=client.loop_forever, daemon=True).start()

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)
