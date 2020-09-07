from random import choice
from armor import Armor
from ability import Ability
from weapon import Weapon


class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer'''
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.return: total_damage:Int '''
        # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def add_armor(self, armor):
        ''' Add armor to self.armors Armor: Armor Object '''
        self.armors.append(armor)

    def defend(self, damage_amt=0):
        '''Calculate the total block amount from all armor blocks. return: total_block:Int '''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        if damage_amt!=0:
            if total_block > damage_amt:
                total_block = damage_amt
        return total_block
    
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        block_amt = self.defend(damage)
        damage_amt = damage
        damage_amt -= block_amt
        self.current_health -= damage_amt

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.'''
        if self.current_health <= 0:
            return False
        else:
            return True
    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills
    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # TODO: This method should add the number of deaths to self.deaths
        self.deaths += num_deaths

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''
        # TODO: Refactor this method to update the following:
        # 1) the number of kills the hero (self) has when the opponent dies.
        # 2) then number of kills the opponent has when the hero (self) dies
        # 3) the number of deaths of the opponent if they die    in the fight
        # 4) the number of deaths of the hero (self) if they die in the fight
        if not self.abilities and not opponent.abilities:
            print("Draw")
        else:
            while self.is_alive() and opponent.is_alive():
                my_attack = self.attack()
                opponent_attack = opponent.attack()
                self.take_damage(opponent_attack)
                opponent.take_damage(my_attack)
            if self.is_alive():
                print(f"{self.name} Won!")
                self.add_kill(1)
                opponent.add_death(1)
            else:
                print(f"{opponent.name} Won!")
                opponent.add_kill(1)
                self.add_death(1)
    

