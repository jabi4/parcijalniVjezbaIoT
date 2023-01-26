from util.JSONSerializator import JSONSerializator

class ConfigDto(JSONSerializator):

    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.publish = False
        self.type = None

    def __repr__(self):
        return str(self.__dict__)