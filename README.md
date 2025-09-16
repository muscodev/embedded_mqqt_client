## ESP8266  MQTT  Publisher
------------------------


# start development

clone the repo

```
python -m venv .venv
pip install -r requirments.txt
```
rename .env_sample to .env

update the .env 

```
# create config.cpp
python setup_config.py

```
Now open the r_module in Arduino IDE

connect the ESP8266 board to the USB port

upload the code


# verify
```
## This will print the sensor data published by esp8266 to the topic
python test/mqqt_test_consumer.py

```


