import tkinter
from tkinter import ttk, IntVar,BooleanVar
import tkinter as tk
from datasource.dto.ConfigDto import ConfigDto



class ConfigComponent(ttk.LabelFrame):

    def __init__(self, parent, row, column):
        super().__init__(master=parent, text="Configuration")
        self.grid(row=row, column=column, padx=5, pady=5)
        self.iotSimulator = parent
        self.setView()

    def setView(self):
        self.temperature = IntVar()
        configTemp = ttk.Scale(self, from_=-30, to=50, variable=self.temperature)
        configTemp.grid(row=0, column=0, pady=5, padx=5)
        lblTemp = ttk.Label(self, textvariable=self.temperature)
        lblTemp.grid(row=0, column=1, padx=5, pady=5)

        self.humidity = IntVar()
        confihHum = ttk.Scale(self, from_=0, to=100, variable=self.humidity)
        confihHum.grid(row=1, column=0, pady=5, padx=5)
        lblHum = ttk.Label(self, textvariable=self.humidity)
        lblHum.grid(row=1, column=1, padx=5, pady=5)

        self.pressure = IntVar()
        configPressure = ttk.Scale(self, from_=-30, to=50, variable=self.pressure)
        configPressure.grid(row=2, column=0, pady=5, padx=5)
        lblPressure = ttk.Label(self, textvariable=self.pressure)
        lblPressure.grid(row=2, column=1, padx=5, pady=5)

        self.simulate = BooleanVar()
        cbSimulate = ttk.Checkbutton(self, text="Simulated", variable=self.simulate)
        cbSimulate.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        btnSaveConfig = ttk.Button(self, text="Save config", command=self.iotSimulator.handleSaveButton)
        btnSaveConfig.grid(row=4, column=0, columnspan=2, pady=5, padx=5, sticky=tk.EW)

    def getConfiguration(self):
        config = ConfigDto()
        config.temperature = self.temperature.get()
        config.humidity = self.humidity.get()
        config.pressure = self.pressure.get()
        config.publish = self.simulate.get()
        return config

    def setConfiguration(self, configDto: ConfigDto):
        if configDto is not None:
            self.temperature.set(configDto.temperature)
            self.humidity.set(configDto.humidity)
            self.pressure.set(configDto.pressure)
            self.simulate.set(configDto.publish)
