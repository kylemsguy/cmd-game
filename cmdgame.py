#!/usr/bin/env python3
import os
from random import randint

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


class Player:
    def __init__(self, name):
        self._name = name
        self._score = 0

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def inc_score(self, value=1):
        self._score += value
        

def maingame():
    game_done = False
    setup_done = False
    used_commands = []
    players = []

    while not setup_done:
        num_players = input("How many players?: ")
        try:
            num_players = int(num_players)

        except ValueError:
            print("Invalid number of players")
            continue

        else:
            if num_players < 1:
                print("Invalid number of players")
            else:
                for i in range(num_players):
                    name = input("What's the name of Player ", i + 1, "?: ",
                                 sep="")
                    new_player = Player(name)
                    players.append(new_player)

                setup_done = True
                # Player set up now done

    #now generate list of commands
    cmd_list = os.listdir("/bin") + os.listdir("/sbin")
    cmd_list = cmd_list + os.listdir("/usr/bin") + os.listdir("/usr/sbin")
    
    
    while not game_done:
        start_letter_index = randint(0, 25)
        start_letter = alphabet[start_letter_index]
        
        
    return 0


if __name__ == "__main__":
    maingame()
