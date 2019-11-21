'''
CTEC 121 Game Example
by Bruce Elgort and Garth Leedle
November 21, 2019

Each player will get 5 weapons

Weapon            Damage Points  Multiplied by Hit or Not(1 or 0)
Daggers           2
Long Sword        3
Broad Sword       3
Two Handed Sword  4
Mace              2
Two Handed Mace   4
Katana            3.5
Short Sword       1.5
Bow               3.5
Crossbow          4

'''

import random
import datetime


class Player:

    weapon_list = ['Dagger', 'Long Sword', 'Broad Sword', 'Two Handed Sword',
                   'Mace', 'Two Handed Mace', 'Katana', 'Short Sword', 'Bow and Arrow', 'Crossbow']

    def __init__(self, id):
        self.weapons = []
        self.health = 0
        self.id = id

        for i in range(5):
            self.weapons.append(
                self.weapon_list[random.randint(0, len(self.weapon_list)-1)])

    def setHealth(self, points):
        self.health += points


def main():

    game_results = open('game_results.txt', 'w')

    weapon_list = {'Dagger': 2, 'Long Sword': 3, 'Broad Sword': 3, 'Two Handed Sword': 4,
                   'Mace': 2, 'Two Handed Mace': 4, 'Katana': 3.5, 'Short Sword': 1.5, 'Bow and Arrow': 3.5, 'Crossbow': 4}
    players = []

    for i in range(100000):
        players.append(Player(i))

    while len(players) > 2:
        print('\n\nStart of battle...')
        print(f'Game Started at {datetime.datetime.now()}')
        game_results.write(f'Game Started at {datetime.datetime.now()}')
        print(60 * '=')
        game_results.write('\n\nStart of battle...\n')
        game_results.write(60 * '=' + "\n")
        player1_index = random.randint(0, len(players)-1)
        player1 = players[player1_index]

        player2_index = random.randint(0, len(players)-1)
        while player1_index == player2_index:
            player2_index = random.randint(0, len(players)-1)
    

        player2 = players[player2_index]

        player_hit = random.randint(0, 1)

        if player_hit == 1:
            player1_hit = 1
            player2_hit = 0
        else:
            player1_hit = 0
            player2_hit = 1

        player1_weapon = player1.weapons[random.randint(
            0, len(player1.weapons)-1)]

        player2_weapon = player1.weapons[random.randint(
            0, len(player2.weapons)-1)]

        if weapon_list[player1_weapon] * player1_hit > weapon_list[player2_weapon] * player2_hit:
            if player1_hit == 1:
                print(
                    f'{player1_weapon} just took out {player2_weapon} with Player {player1.id} winning the hit')
                game_results.write(
                    f'{player1_weapon} just took out {player2_weapon} with Player {player1.id} winning the hit\n')
            else:
                print(
                    f'{player2_weapon} just took out {player1_weapon} with Player {player2.id} winnin the hit')
                game_results.write(
                    f'{player2_weapon} just took out {player1_weapon} with Player {player2.id} winnin the hit\n')

            player1.setHealth(weapon_list[player1_weapon])
            player2.setHealth(weapon_list[player2_weapon] * -1)
        else:
            if player2_hit == 1:
                print(
                    f'{player2_weapon} just took out {player1_weapon} with player {player2.id} winning the hit')
                game_results.write(
                    f'{player2_weapon} just took out {player1_weapon} with player {player2.id} winning the hit\n')
            else:
                print(
                    f'{player1_weapon} just took out {player2_weapon} with player {player1.id} winning the hit')
                game_results.write(
                    f'{player1_weapon} just took out {player2_weapon} with player {player1.id} winning the hit\n')

            player2.setHealth(weapon_list[player2_weapon])
            player1.setHealth(weapon_list[player1_weapon] * -1)

        if player1.health < 0:
            del players[player1_index]
        elif player2.health < 0:
            del players[player2_index]

        print(f'Player {player1.id} health: {player1.health}')
        game_results.write(f'Player {player1.id} health: {player1.health}\n')
        print(f'Player {player2.id} health: {player2.health}')
        game_results.write(f'Player {player2.id} health: {player2.health}\n')

    if player1.health > player2.health:
        print(f'\n\nThe player with ID of {player1.id} won ')
        game_results.write(f'\n\nThe player with ID of {player1.id} won')
    else:
        print(f'\n\nThe player with ID of {player2.id} won ')
        game_results.write(f'\n\nThe player with ID of {player2.id} won\n')

    game_results.close()


main()
