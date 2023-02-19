from abc import ABC, abstractmethod
from Entity import Entity

class Creeper(Entity):

    def __init__(self):
        pass
    
    @abstractmethod
    def explode(self):
        pass
