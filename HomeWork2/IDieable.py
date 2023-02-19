from abc import ABC, abstractmethod

class IDieable(ABC):
    @abstractmethod
    def die(self):
        pass