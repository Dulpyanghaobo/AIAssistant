from abc import ABC, abstractmethod

class IInputProcessor(ABC):
    @abstractmethod
    def process(self, input_data):
        pass





