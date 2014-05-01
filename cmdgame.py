#!/usr/bin/env python3
import os
import re
from random import randint

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


class Player:
    def __init__(self, index, name):
        self._name = name
        self._index = index
        self._score = 0

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def get_index(self):
        return self._index

    def inc_score(self, value=1):
        self._score += value
        

def maingame():
    game_done = False
    setup_done = False
    used_commands = []
    letter_blacklist = []
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
                    print("What's the name of Player ", i + 1, "?: ",
                                 sep="", end="")
                    name = input()
                    new_player = Player(i+1, name)
                    players.append(new_player)

                setup_done = True
                # Player set up now done

    #now generate list of commands
    cmd_list = os.listdir("/bin") + os.listdir("/sbin")
    cmd_list = cmd_list + os.listdir("/usr/bin") + os.listdir("/usr/sbin")

    start_letter_index = -1
    last_start_letter = -1
    while not game_done:
        if len(letter_blacklist) == 26 or len(used_commands) >= 100:
            break # end game
        last_start_letter = start_letter_index
        start_letter_index = randint(0, 25)
        if start_letter_index == last_start_letter:
            continue
        start_letter = alphabet[start_letter_index]
        letter_pattern = re.compile(start_letter)
        no_cmd = True
        for command in cmd_list:
            if not command in used_commands:            
                if re.match(letter_pattern, command):
                    no_cmd = False
                    break
                else:
                    continue

        if no_cmd:
            letter_blacklist.append(start_letter)
            continue
        else:
            for player in players:
                print("The letter is", start_letter)
                print("Player ", player.get_index(), "'s turn.", sep="")
                print(player.get_name(), "please enter your guess: ", end="")
                guess = input()
                if guess in used_commands:
                    print("Command used already. You lose your turn.")
                    continue
                elif not guess in cmd_list:
                    print("Not a valid command. You lose your turn.")
                    continue
                else:
                    used_commands.append(guess)
                    print("Congrats! You earn one point.")
                    player.inc_score()
                    
    # game end stuff
    print("The scores are:")
    for player in players:
        print(player.get_name(), end="\t")
    for player in players:
        print(player.get_score())
        


if __name__ == "__main__":
    maingame()
