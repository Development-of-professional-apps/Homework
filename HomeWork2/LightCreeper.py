from Creeper import Creeper
from IDieable import IDieable

class LightCreeper(Creeper, IDieable):

    def __init__(self):
        pass

    def explode(self):
        print("Explodes with light")
    
    def die(self):
        print("Dies with light")