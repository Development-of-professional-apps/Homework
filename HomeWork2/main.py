from ElectricCreeper import ElectricCreeper
from LightCreeper import LightCreeper

if __name__ == '__main__':
    creepers = [ElectricCreeper(), LightCreeper()]

    for c in creepers:
        c.explode()   
    print('')
    for c in creepers:
        c.die()
    
    electricCreeper = ElectricCreeper()

    print(electricCreeper.getExample())
    electricCreeper.setExample(10)
    print(electricCreeper.getExample())