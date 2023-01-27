from threading import Thread
from mqtt.MqttClient import MqttClient
from service.ConfigurationService import ConfigurationService
from time import sleep as delay


class Publisher(Thread):

    def __init__(self, mqtt: MqttClient, type):
        super().__init__()
        self.mqtt = mqtt
        self.type = type
        self.configDto = None

    def update(self, configDto):
        self.configDto = configDto


    def run(self):
        service = ConfigurationService()
        while True:
            if self.configDto is not None:
                if self.configDto.publish:
                    self.mqtt.publish(self.configDto.getJson(), f"parcijalni/{self.type}JB")
            else:
                self.configDto = service.readConfiguration(self.type)

            delay(10)



