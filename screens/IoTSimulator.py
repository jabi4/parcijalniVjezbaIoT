from tkinter import ttk, LabelFrame, Frame
import tkinter as tk
from PIL import Image, ImageTk
from mqtt.MqttClient import MqttClient
from components.SelectTypeComponent import SelectTypeComponent
from components.ConfigComponent import ConfigComponent, ConfigDto




class IoTSimulator(Frame):

    SERVER_URL = "edu-agrdan.plusvps.com"

    def __init__(self, parent):
        super().__init__(master=parent)

        self.mqtt = MqttClient(self.SERVER_URL, 1883, "parcijalni/+")
        self.mqtt.start()
        self.grid()
        self.setView()


    def setView(self):
        self.typeSelect = SelectTypeComponent(self, 0, 0)
        self.configSelect = ConfigComponent(self, 0, 1)

    def handleRadioButton(self):
        self.type = self.typeSelect.choices[self.typeSelect.radioValue.get()]
        print(self.type)

    def handleSaveButton(self):
        self.handleRadioButton()
        configDto = self.configSelect.getConfiguration()
        configDto.type = self.type
        print(configDto)





