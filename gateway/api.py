import os
import uuid
import asyncio
from pytradfri.api.aiocoap_api import APIFactory
from pytradfri import Gateway

loop = asyncio.get_event_loop()

class Api:
    def __init__(self):
        pass

    async def async_init(self):
        self.api_factory = await self._create_api_factory()
        self.request = self.api_factory.request
        self.myGateway = Gateway()

    async def _create_api_factory(self):
        assert "GATEWAY_IP" in os.environ and "GATEWAY_KEY" in os.environ, "Gateway IP or key missing"
        host = os.environ["GATEWAY_IP"]
        key = os.environ["GATEWAY_KEY"]
        identity = uuid.uuid4().hex
        api_factory = APIFactory(host=host, psk_id=identity)
        await api_factory.generate_psk(key)
        return api_factory

    async def async_get_devices(self):
        devices_command = await self.request(self.myGateway.get_devices())
        self.devices = await self.request(devices_command)

    async def async_set_dimmer(self, light, level):
        command = light.light_control.set_dimmer(level)
        await self.request(command)

    def get_devices(self, only_lights = False):
        loop.run_until_complete(self.async_get_devices())
        if only_lights:
            lights = []
            for device in self.devices:
                if device.has_light_control:
                    lights.append(device)
            return lights
        else:
            return self.devices

    def get_device_by_name(self, name):
        loop.run_until_complete(self.async_get_devices())
        for device in self.devices:
            if device.name == name:
                return device
        return None




  
 
