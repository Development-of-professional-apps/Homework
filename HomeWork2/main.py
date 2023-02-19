from abc import ABC, abstractmethod

class Vector3:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Entity(ABC):
    position = Vector3(0, 0, 0)

    def __init__(self):
        pass


class Creeper(Entity):

    def __init__(self):
        pass
    
    @abstractmethod
    def explode(self):
        pass


class ElectricCreeper(Creeper):

    def __init__(self):
        pass

    def explode(self):
        print("Explodes with electricity")


class LightCreeper(Creeper):

    def __init__(self):
        pass

    def explode(self):
        print("Explodes with light")

if __name__ == '__main__':
    
    creepers = [ElectricCreeper(), ElectricCreeper()]

    for c in creepers:
        c.explode()
