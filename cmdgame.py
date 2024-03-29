#!/usr/bin/env python3
import os
import re
from random import randint, shuffle

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

GAME_LIMIT = 15

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

    def __str__(self):
        return self.get_name()

def get_other_commands(cmd_filename="other_commands.txt"):
    comment_pat = re.compile('#')
    add_pat = re.compile('+')
    remove_pat = re.compile('-')

    cmd_file = open(cmd_filename, 'r')

    

def get_commands(force=False):
    if os.name != "posix" and not force:
        raise OSError
    cmd_list = os.listdir("/bin") + os.listdir("/sbin")
    cmd_list = cmd_list + os.listdir("/usr/bin") + os.listdir("/usr/sbin")
    return list(set(cmd_list))

def setup_players():
    players = []
    setup_done = False
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
    return players[:] #return the player list (deep copy)

def maingame():
    game_done = False
    used_commands = []
    letter_blacklist = []
    players = []

    #generate list of commands
    try:
        cmd_list = get_commands()
    except OSError:
        print("OS not supported. Continue? [Y/n] ", end="")
        go = input()
        if go == "n":
            return # end the game now.
        else:
            cmd_list = get_commands(True)

    # get number of players and make player objects
    players = setup_players()

    # randomize the list of players
    player_indices = list(range(len(players))) # get a list of indices
    
    start_letter_index = -1
    last_start_letter = 0
    err = False

    # main game loop
    while not game_done:
        if len(letter_blacklist) == 26 or len(used_commands) >= GAME_LIMIT:
            break # end game

        if not err:
            # score standings
            print("\nThis is how the scores stand:")
            for player in players:
                print(player.get_name(), end="\t")
            print()
            for player in players:
                print(player.get_score(), end="\t")
            print()
        else:
            err = False

        # shuffle players
        shuffle(player_indices)
        
        start_letter_index = randint(0, 25)
        if start_letter_index == last_start_letter:
            err = True
            continue
        last_start_letter = start_letter_index
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
            err = True
            continue
        else:
            for index in player_indices:
                player = players[index]
                print("The letter is", start_letter)
                print("Player ", player.get_index(), "'s turn.", sep="")
                print(player.get_name(), "please enter your guess: ", end="")
                guess = input()
                if guess in used_commands:
                    print("Command used already. You lose a point.")
                    player.inc_score(-1)
                    continue
                elif not guess in cmd_list:
                    print("Not a valid command. You lose your turn.")
                    continue
                else:
                    used_commands.append(guess)
                    print("Congrats! You earn one point.")
                    player.inc_score()
                    break
                    
    # game end stuff
    print("\nThe scores are:")
    for player in players:
        print(player.get_name(), end="\t")
    print()
    for player in players:
        print(player.get_score(), end="\t")

    max_players = []
    max_score = 0
    for player in players:
        if player.get_score() > max_score:
            max_players = [player]
            max_score = player.get_score()
        elif player.get_score() == max_score > 0:
            max_players.append(player)
        else:
            continue

    if len(max_players) > 1:
        print("\n\nThe winners are ")
        for player in max_players:
            print(player.get_name(), sep="\t")
    else:
        print("\n\nThe winner is", max_players[0].get_name())

if __name__ == "__main__":
    maingame()
