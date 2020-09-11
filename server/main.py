from flask import Flask, request
from gateway import api
import asyncio

loop = asyncio.get_event_loop()
myAPI = api.Api()
loop.run_until_complete(myAPI.async_init())

app = Flask(__name__)

@app.route('/lights/<name>/<level>', methods=["POST"]) 
def lights(name, level):
    device = myAPI.get_device_by_name(name)
    if device:
        loop.run_until_complete(myAPI.async_set_dimmer(device,int(level)))
        return "OK", 200
    return "Light not found", 404

@app.route('/lights/all/<level>', methods=["POST"]) 
def all_lights(level):
    devices = myAPI.get_devices(only_lights=True)
    for device in devices:
        loop.run_until_complete(myAPI.async_set_dimmer(device,int(level)))
    return "OK", 200
  
            