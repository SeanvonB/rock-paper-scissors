#!/usr/bin/env python3


import random


moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.score = 0
    
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "You"

   
class RockPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Dwayne Johnson"


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Henry Zebrowski"

    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "John Kem Poe"


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "RoShamBot 3000"


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
        if beats(move1, move2):
            self.p1.score += 1
            print(f"That's a point for {self.p1.name}!""\n")
        elif beats(move2, move1):
            self.p2.score += 1
            print(f"That's a point for {self.p2.name}!""\n")
        else:
            print("It's a draw!""\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        round = 0
        print("Game start!")
        while self.p1.score <= 1 and self.p2.score <= 1:
            round += 1
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score == 2:
            print(f"{self.p1.name} win! Congratulations!")
        else:
            print(f"{self.p2.name} wins! Better luck next time!")


if __name__ == '__main__':
    game = Game(RockPlayer(), RandomPlayer())
    game.play_game()
