from tkinter import Tk
from screens.IoTSimulator import IoTSimulator
class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("Ponavljanje parcijalni IoT")
        self.geometry("600x400")
        self.createIoT()

    def createIoT(self):
        IoTSimulator(self)



if __name__ == '__main__':
    app = App()
    app.mainloop()

