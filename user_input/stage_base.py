
class StageBase:
    def __init__(self,name,type):
        self._name = name
        self._type = type 

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

