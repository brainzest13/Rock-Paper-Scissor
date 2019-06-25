#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random
moves = ['rock', 'paper', 'scissors']


# exit the game
def stop():
    print('\nThanks for playing!')
    sys.exit()


class Player:

    score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer (Player):
    def __init__(self):
        Player.__init__(self)  # subclass of Player

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    # subclass of Player
    def __init__(self):
        Player.__init__(self)

    def move(self):
        x = input(" What would you like to throw? \n")
        while x not in moves and x != "z" and x != "quit":
            x = input("Please enter a valid throw: "
                      "rock, paper, scissors, or z or quit \n")

        if x == "z" or x == "quit":
            stop()
        return x


class ReflectPlayer(Player):
    """
        Reflect player class: remembers what move the opponent played last
        round, and plays that move this round.
    """
    def __init__(self):
        """Initialize a ReflectPlayer instance."""
        Player.__init__(self)
        self.last_player_move = None
        self.my_move = None

    def move(self):
        """Return the player move in a string (last opponent move)."""
        if self.last_player_move is None:
            return Player.move(self)
        return self.last_player_move

    def learn(self, last_player_move, my_move):
        self.last_player_move = last_player_move


class CyclePlayer(Player):
    """
        Cycle player class: remembers what move it played last round, and
        cycles through the different moves.
    """
    def __init__(self):
        """Initialize a CyclePlayer instance derived from Player Class"""
        Player.__init__(self)
        self.last_move = None
        self.last_player_move = None

    def move(self):
        """Return the player move in a string (cycle)."""
        curr_move = None
        if self.last_move is None:
            curr_move = Player.move(self)
        else:
            index = moves.index(self.last_move) + 1
            if index >= len(moves):
                index = 0
            curr_move = moves[index]
        self.last_move = curr_move
        return curr_move

    def learn(self, last_player_move, last_move):
        self.last_move = last_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move1, move2)

        if beats(move1, move2):
            self.p1.score += 1
            print("Player 1 wins this round ")

        elif beats(move2, move1):
            self.p2.score += 1
            print("Player 2 wins this round")
        else:
            print("It's a Tie! No Points added.")

        print(f"\n----Scores----\n Player 1: {self.p1.score}"
              f" \n Player 2:{self.p2.score} \n")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()

        print("\n Game over!")
        print(f"\n----- Final Scores ----\n\n Player 1: {self.p1.score}"
              f" \n Player 2: {self.p2.score} \n")
        if self.p1.score > self.p2.score:
            print("Player 1 Wins the Game!")
            stop()
        elif self.p2.score > self.p1.score:
            print("Player 2 Wins the Game!")
            stop()
        else:
            print("It's a tie!")
            stop()


if __name__ == '__main__':

    askPlayer = 'Play either "rock", "paper", or "scissors" ' \
                'If you want to stop playing,' \
                'enter a "z" or "quit". \n Who would you like to play with? ' \
                'Please enter "random", "reflect", "repeat", or "cycle" \n '

    list_of_players = {'repeat': Player(),
                       'random': RandomPlayer(),
                       'reflect': ReflectPlayer(),
                       'cycle': CyclePlayer()
                       }
    choice = input(askPlayer)
    if choice == "quit" or choice == "z":
        print('\nThanks for playing!')
    else:
        while choice not in list_of_players:
            choice = input('\n Please select a valid player,'
                           ' "random", "reflect", "repeat", or "cycle" \n ')

        game = Game(HumanPlayer(), list_of_players[choice])
        game.play_game()
