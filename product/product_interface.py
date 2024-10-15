from abc import ABC, abstractmethod

class ProductInterface(ABC):
    @property
    @abstractmethod
    def scheduled_time(self):
        pass

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def deploy(self):
        pass

    @abstractmethod
    def notify(self):
        pass