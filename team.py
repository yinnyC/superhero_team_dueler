import random
from hero import Hero



class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes'''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list. If Hero isn't found return 0.'''
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to True
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their names to the terminal one by one.
        hero_name = [hero.name for hero in self.heroes]
        print(",".join(hero_name))

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # TODO: Add the Hero object that is passed in to the list of heroes in self.heroes
        self.heroes.append(hero)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            if hero.deaths !=0 and hero.kills !=0:
                kd = str(hero.kills / hero.deaths)
                print("{} Kill/Deaths:{}".format(hero.name, kd))
            else:
                print("{} Kill/Deaths: N/A".format(hero.name))

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: for each hero in self.heroes,
        # set the hero's current_health to their starting_health
        for hero in self.heroes:
            hero.current_health = hero.starting_health
    def attack(self, other_team):
        ''' Battle each team against each other.'''
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            pick_hero = random.choice(living_heroes)
            pick_opponent = random.choice(living_opponents)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            pick_hero.fight(pick_opponent)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight
            if pick_hero.is_alive():
                living_opponents.remove(pick_opponent)
            else:
                living_heroes.remove(pick_hero)

            
