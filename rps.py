#!/usr/bin/env python3

import random

moves = ['rock', 'paper', 'scissors']

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class HumanPlayer(Player):
    pass
    
class RockPlayer(Player):
    self.name = "Dwayne Johnson"
    def __init__(self):
        super().__init__()

class RandomPlayer(Player):
    self.name = "Henry Zebrowski"
    def __init__(self):
        super().__init__()
    def move(self):
        return random.choice(moves)

class ReflectPlayer(Player):
    self.name = "John Kem Poe"
    def __init__(self):
        super().__init__()

class CyclePlayer(Player):
    self.name = "RoShamBot 3000"
    def __init__(self):
        super().__init__()


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
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
