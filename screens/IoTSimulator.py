from tkinter import ttk, LabelFrame, Frame
from mqtt.MqttClient import MqttClient
from components.SelectTypeComponent import SelectTypeComponent, TypeEnum
from components.ConfigComponent import ConfigComponent, ConfigDto
from service.ConfigurationService import ConfigurationService
from service.Publisher import Publisher





class IoTSimulator(ttk.Frame):

    SERVER_URL = "edu-agrdan.plusvps.com"

    def __init__(self, parent):
        super().__init__(master=parent)
        self.grid()
        self.mqtt = MqttClient(self.SERVER_URL, 1883, "parcijalni/+")
        self.mqtt.start()
        self.enum = TypeEnum
        self.configurationService = ConfigurationService()
        self.publishIndoor = Publisher(self.mqtt, self.enum.INDOOR.value)
        self.publishIndoor.start()
        self.publishOutdoor = Publisher(self.mqtt, self.enum.OUTDOOR.value)
        self.publishOutdoor.start()
        self.publishCity = Publisher(self.mqtt, self.enum.CITY.value)
        self.publishCity.start()

        self.setView()
        self.setupConfig()


    def setView(self):
        self.typeSelect = SelectTypeComponent(self, 0, 0)
        self.configSelect = ConfigComponent(self, 0, 1)

    def handleRadioButton(self):
        self.setupConfig()

    def setupConfig(self):
        self.type = self.typeSelect.choices[self.typeSelect.radioValue.get()]
        configDto: ConfigDto = self.configurationService.readConfiguration(self.type)
        if configDto is not None:
            self.configSelect.setConfiguration(configDto)
        else:
            empty = ConfigDto()
            self.configSelect.setConfiguration(empty)

    def handleSaveButton(self):
        configDto = self.configSelect.getConfiguration()
        configDto.type = self.typeSelect.choices[self.typeSelect.radioValue.get()]
        self.configurationService.insertOrUpdate(configDto)
        match configDto.type:
            case self.enum.INDOOR:
                self.publishIndoor.update(configDto)
            case self.enum.OUTDOOR:
                self.publishOutdoor.update(configDto)
            case self.enum.CITY:
                self.publishCity.update(configDto)





