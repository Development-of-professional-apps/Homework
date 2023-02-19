from Creeper import Creeper
from IDieable import IDieable

class ElectricCreeper(Creeper, IDieable):

    def __init__(self):
        pass

    def explode(self):
        print("Explodes with electricity")
    
    def die(self):
        print("Dies with electricity")