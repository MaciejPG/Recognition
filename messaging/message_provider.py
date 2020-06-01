from abc import ABC, abstractmethod

class MessageProvider(ABC):
    @abstractmethod
    def send(self, message: str):
        pass
    
