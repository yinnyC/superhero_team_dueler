from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.
        self.team_one = Team("team_one")
        self.team_two = Team("team_two")

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = int(input("What is the max damage of the ability?  "))
        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        name = input("What is the weapon name?  ")
        max_damage = int(input("What is the max damage of the weapon?  "))
        # return the new weapon object.
        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor object.
        name = input("What is the armor name?  ")
        max_block = int(input("What is the max block of the armor?  "))
        #  return the new armor object with values set by user.
        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input(
                "[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                # TODO add an ability to the hero
                # HINT: First create the ability, then add it to the hero
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                # TODO add a weapon to the hero
                # HINT: First create the weapon, then add it to the hero
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                # TODO add an armor to the hero
                # HINT: First create the armor, then add it to the hero
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero
    # build_team_one is provided to you

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        # Add the created hero to team one.
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for _ in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    # Now implement build_team_two
    # HINT: If you get stuck, look at how build_team_one is implemented
    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        numOfTeamMembers = int(
            input("How many members would you like on Team Two?\n"))
        # call self.create_hero() for every hero that the user wants to add to team two.
        for _ in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)  # Add the created hero to team two.

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        self.team_one.attack(self.team_two)

    def show_kd(self,team):
        ''' calculate the average K/D for the team. '''
        team_kills = 0
        team_deaths = 0
        for hero in team.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        kd = team_kills/team_deaths
        print(f"{team.name} average K/D was: {kd}" )
    def show_survive_heros(self,team):
        for hero in team.heroes:
            if hero.deaths == 0:
                print(f"survived from {team.name}: {hero.name}")
    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print(f"\n{self.team_one.name} statistics: ")
        self.team_one.stats()
        print(f"\n{self.team_two.name} statistics: ")
        self.team_two.stats()
        print("\n")
        # This is how to calculate the average K/D for Team One
        self.show_kd(self.team_one)
        # TODO: Now display the average K/D for Team Two
        self.show_kd(self.team_two)
        # Here is a way to list the heroes from Team One that survived
        self.show_survive_heros(self.team_one)
        #TODO: Now list the heroes from Team Two that survived
        self.show_survive_heros(self.team_two)


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()