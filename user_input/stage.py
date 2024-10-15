from user_input.stage_base import StageBase

class Stage(StageBase):
    def __init__(self, name:str, type:str,args:dict):
        super().__init__(name, type)
        self._args = args
        
    @property
    def args(self):
        return self._args

    @args.setter
    def args(self, value):
        self._args = value

    def __str__(self):
        return f"Stage(name={self.name}, type={self.type}, args={self.args})"