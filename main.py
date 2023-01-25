from tkinter import Tk
from screens.mainScreen import ConfigScreen
class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("Config")
        self.geometry("600x400")
        self.createServerConnection()

    def createServerConnection(self):
        ConfigScreen(self)





if __name__ == '__main__':
    app = App()
    app.mainloop()

