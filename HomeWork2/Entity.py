from abc import ABC, abstractmethod
from Vector3 import Vector3

class Entity(ABC):
    __example = 0 # Пример инкапсуляции
    position = Vector3(0, 0, 0)

    def __init__(self):
        pass
    
    def getExample(self) -> int:
        return self.__example
    
    def setExample(self, example):
        self.__example = example