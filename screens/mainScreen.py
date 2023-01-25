from tkinter import ttk, LabelFrame, Frame
import tkinter as tk
from PIL import Image, ImageTk






class ConfigScreen(LabelFrame):

    def __init__(self, mainWindow):
        super().__init__(master=mainWindow)
        self.grid(padx=5, pady=5)
        self._loadImages()
        self.createConnectionsFrame()


    def createConnectionsFrame(self):

        self.lblCity = ttk.Label(self, image=self.tkImgCity)
        self.lblCity.grid(row=0, column=0, pady=5, padx=5)

        self.lblHouse = ttk.Label(self, image=self.tkImgHouse)
        self.lblHouse.grid(row=1, column=0, pady=5, padx=5)

        self.lblPark = ttk.Label(self, image=self.tkImgPark)
        self.lblPark.grid(row=2, column=0, pady=5, padx=5)

        self.radioBtnCity = tk.Radiobutton(self, value="City")
        self.radioBtnCity.grid(row=0, column=1, pady=5, padx=5)

        self.radioBtnHouse = tk.Radiobutton(self)
        self.radioBtnHouse.grid(row=1, column=1, padx=5, pady=5)

        self.radioBtnPark = tk.Radiobutton(self)
        self.radioBtnPark.grid(row=2, column=1, padx=5, pady=5)


    def _loadImages(self):
        imgCity = Image.open("./images/city.png")
        imgHouse = Image.open("./images/house.png")
        imgPark = Image.open("./images/park.png")

        self.tkImgCity = ImageTk.PhotoImage(imgCity)
        self.tkImgHouse = ImageTk.PhotoImage(imgHouse)
        self.tkImgPark = ImageTk.PhotoImage(imgPark)
