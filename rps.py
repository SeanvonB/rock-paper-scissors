#!/usr/bin/env python3


import random


moves = ["rock", "paper", "scissors"]


valid_rock = {
        "rock": "rock",
        "Rock": "rock",
        "ROCK": "rock",
        "r": "rock"}

valid_paper = {
        "paper": "paper",
        "Paper": "paper",
        "PAPER": "paper",
        "p": "paper"}

valid_scissors = {
        "scissors": "scissors",
        "Scissors": "scissors",
        "SCISSORS": "scissors",
        "scissor": "scissors",
        "s": "scissors"}

valid_menu_single = {
        "single": "single",
        "Single": "single",
        "SINGLE": "single",
        "single round": "single",
        "Single Round": "single",
        "1": "single"}

valid_menu_endless = {
        "endless": "endless",
        "Endless": "endless",
        "ENDLESS": "endless",
        "endless_mode": "endless",
        "Endless Mode": "endless",
        "2": "endless"}

valid_continue = {
        "yes": "yes",
        "yes please": "yes",
        "yeah": "yes",
        "yup": "yes",
        "y": "yes",
        "sure": "yes",
        "okay": "yes"}


class Player:
    def __init__(self):
        self.score = 0
        self.my_last = None
        self.their_last = None

    def learn(self, my_move, their_move):
        self.my_last = my_move
        self.their_last = their_move

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "You"

    def move(self):
        choice = 0
        fails = 0
        while choice == 0:
            if fails == 0:
                move_choice = str(input(
                    "\nWhat will you throw: "
                    "Rock, Paper, or Scissors? "))
            else:
                move_choice = str(input(
                    "\nTry again: "
                    "Rock, Paper, or Scissors? "))
            if move_choice in valid_rock:
                choice = "rock"
            elif move_choice in valid_paper:
                choice = "paper"
            elif move_choice in valid_scissors:
                choice = "scissors"
            else:
                if fails <= 2:
                    fails += 1
                    print(
                        "\n'Flag on the play!"
                        f"The referee rules that '{move_choice}' "
                        "isn't a tournament-legal throw!'")
                else:
                    choice = random.choice(moves)
                    print(
                        "\n'The referee rules that "
                        "the garbage you're throwing "
                        f"most closely resembles {choice}!'")
        return choice


class RockPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Dwayne Johnson"

    def move(self):
        return "rock"


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Henry Zebrowski"


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "John Kem Poe"

    def move(self):
        if self.their_last is None:
            return random.choice(moves)
        else:
            return self.their_last


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "RoShamBot 3000"

    def move(self):
        if self.my_last is None:
            return random.choice(moves)
        else:
            if self.my_last == "rock":
                return "paper"
            elif self.my_last == "paper":
                return "scissors"
            else:
                return "rock"


opponent = [
    RockPlayer(),
    RandomPlayer(),
    ReflectPlayer(),
    CyclePlayer()]


def beats(one, two):
    return ((one == "rock" and two == "scissors") or
            (one == "scissors" and two == "paper") or
            (one == "paper" and two == "rock"))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(
            f"\nPlayer 1: {move1.capitalize()}  "
            f"Player 2: {move2.capitalize()}")
        if beats(move1, move2):
            self.p1.score += 1
            print(
                "'That's a point for you! "
                f"You have {self.p1.score}, "
                f"and {self.p2.name} has {self.p2.score}.'")
        elif beats(move2, move1):
            self.p2.score += 1
            print(
                f"'That's a point for {self.p2.name}! "
                f"He has {self.p2.score}, "
                f"and you have {self.p1.score}.'")
        else:
            print(
                "'It's a draw! "
                f"{self.p2.name} still has {self.p2.score}, "
                f"and you still have {self.p1.score}.'")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_endless(self):
        round = 0
        print(f"\nYou're playing against {self.p2.name}. Begin!")
        while self.p1.score <= 1 and self.p2.score <= 1:
            round += 1
            print(f"\nRound {round}:")
            self.play_round()
        if self.p1.score == 2:
            print(f"\n'You win! Congratulations!'")
            print(
                f"You beat {self.p2.name} "
                "with a score of "
                f"{self.p1.score} to {self.p2.score}.")
        else:
            print(f"\n'{self.p2.name} wins! Better luck next time!'")
            print(
                f"{self.p2.name} beat you "
                "with a score of "
                f"{self.p2.score} to {self.p1.score}.")
        keep_playing = str(input("\nContinue? "))
        if keep_playing in valid_continue:
            game = Game(HumanPlayer(), random.choice(opponent))
            game.play_endless()
        else:
            print("\n'Thanks for playing!'")

    def play_single(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nYou: {move1}  Opponent: {move2}")
        if beats(move1, move2):
            print("'You win! Congratulations!'")
        elif beats(move2, move1):
            print("'You lose! Better luck next time!'")
        else:
            print("'It's a draw!")
        keep_playing = str(input("\nReturn to the Main Menu? "))
        if keep_playing in valid_continue:
            game = Game(HumanPlayer(), random.choice(opponent))
            game.menu()
        else:
            print("\n'Thanks for playing!'")

    def menu(self):
        selection = 0
        print("\n'Welcome to Rock-Paper-Scissors Simulator 2018!'")
        while selection == 0:
            game_type = str(input(
                "\n[1] Play Single Round\n"
                "[2] Play Endless Mode\n"
                "\nPlease select a game type: "))
            if game_type in valid_menu_single:
                selection = 1
                game = Game(HumanPlayer(), random.choice(opponent))
                game.play_single()
            elif game_type in valid_menu_endless:
                selection = 1
                game = Game(HumanPlayer(), random.choice(opponent))
                game.play_endless()
            else:
                keep_playing = str(input("\nExit game? "))
                if keep_playing in valid_continue:
                    selection = 1
                    print("\n'Thanks for playing!'")


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(opponent))
    game.menu()
