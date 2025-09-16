# map pin to sensor name for UI

SENSOR_MAP = {
    "0": "Gate 1",
    "4": "Gate 2",
    "5": "Button 1",
    "12": "Button 2",
    "14": "Proxymit",
}


def mappintoSensor(data: dict) -> dict:
    return {SENSOR_MAP.get(k, k): v for k, v in data.items()}
