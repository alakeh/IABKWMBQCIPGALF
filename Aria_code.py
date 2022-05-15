import sys
from argparse import ArgumentParser
import random as r

board = {
    0: "normal",
    1: "chance",
    2: "normal",
    3: "normal",
    4: "normal",
    5: "normal",
    6: "downbad",
    7: "normal",
    8: "chance",
    9: "normal",
    10: "normal",
    11: "normal",
    12: "downbad",
    13: "chance",
    14: "normal",
    15: "normal",
    16: "downbad",
    17: "downbad",
    18: "normal",
    19: "normal",
    20: "normal",
    21: "chance",
    22: "normal",
    23: "normal",
    24: "normal",
    25: "chance",
    26: "downbad",
    27: "normal",
    28: "normal",
    29: "jackpot"
}


class Game:
    """ A class to play the game.

    Attributes:
        name0(string): player 1's name.
        name1(string): player 2's name.
        name2(string): player 3's name.
        win_condition(int): optional parameter of how many crown points are needed to win
    """

    def __init__(self, name0, name1, name2, win_condition = 5):
        """ Initializes game objects.
        Args:
            name0(string): player 1's name.
            name1(string): player 2's name.
            name2(string): player 3's name.
        Side effect:
            Sorts the order of players
            Sets position, coin count, and crown count dictionaries to 0
            Reassign attribute names
        """
        self.players = sorted([name0, name1, name2], key = str.lower)
        self.player_position = {name: 0 for name in self.players}
        self.coin_count = {name: 0 for name in self.players}
        self.crown_count = {name: 0 for name in self.players}
        self.win_condition = win_condition






    def play_round(self, round_number):
        """Manages a single round in the game
        Args:
            round_number(int):Number of rounds that have been played since the game started
        Side effect:
            Returns end_game if game is ready to finish
            Prints the updated coins, crown points, and positions.
            Prints messages to prompt player through coin toss with result.
        """
        if round_number % 3 == 0:
            self.rock_paper_scissors()
            print(str(self))
        end_game = False

        for player in self.players:
            print(f"\nIT IS NOW {player.upper()}'S TURN")
            playerChoice = int(input("Choose: 1 (Heads) or 2 (Tails)"))
            compChoice = r.randrange(1, 3)
            die_roll = 0
            while playerChoice > 2 or playerChoice < 1:
                playerChoice = int(input("Please enter a valid input: "))
            if playerChoice == compChoice:
                print("Good pick! You will be rolling from 1-12!")
                die_roll = r.randrange(1, 13)
            else:
                print("Better luck next time, you will be rolling from 1-6!")
                die_roll = r.randrange(1, 7)
            position = self.player_move(player, die_roll)
            self.process_tile(player, position)
            self.add_crown(player)
            end_game = self.is_game_over(player, self.win_condition)
            if end_game:
                break
        return not end_game

    def add_crown(self, player):
        """When a player reaches 35 coins, coins will be subtracted and a crown point will be added.
        Args:
            player(str): Player whose turn it is.
        Side Effects:
            Updates the coin counter and the crown counter to reflect exchange
            Prints sentence to inform player that exchange has been made
        """
        if self.coin_count[player] >= 35:
            print(f"Congrats, {player} will now trade 35 coins for a crown point! Wowee!")
            self.coin_count[player] -= 35
            self.crown_count[player] += 1




    def __str__(self):
        """ Magic Method that displays the coin count, crown point count, and board position
        of each player participating in the game.

        Returns:
            Returns an updated display of all coin counts, crown point counts, and player positions.
        Side Effects:
            Updates appropriate displays.
        """
        result = "\nPOSITIONS\n"
        for player, pos in self.player_position.items():
            result += f"Player - {player}, Space - {pos + 1}\n"
        result += "\nCOINS\n"
        for player, coins in self.coin_count.items():
            result += f"Player - {player}, Coins - {coins}\n"
        result += "\nCROWNS\n"
        for player, crowns in self.crown_count.items():
            result += f"Player - {player}, Crowns - {crowns}\n"
        return result



if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    the_game = Game(args.name0, args.name1, args.name2, args.win_condition)
    round_counter = 1
    print(str(the_game))
    while the_game.play_round(round_counter):
        round_counter += 1
        print(str(the_game))