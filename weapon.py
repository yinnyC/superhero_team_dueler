import random 
from ability import Ability

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        random_value = random.randint(self.max_damage//2,self.max_damage)
        return random_value 

