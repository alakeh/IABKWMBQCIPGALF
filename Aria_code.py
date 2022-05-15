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

    def player_move(self, player, die_roll):
        """Rolls the die and moves the player the appropriate amount of spaces.
        Args:
            player(str): Player whose turn it is.
            die_roll(int between 1-6): Players roll on the die.
        Returns:
            The player's current position
        Side effect:
            Updates player position.
        """
        self.player_position[player] += die_roll
        self.player_position[player] %= len(board)
        position = self.player_position[player] + 1
        print(f"You rolled a {die_roll}!")
        print(f"{player}'s new position is tile {position}"
              f", and you landed on a {board[position - 1]} space")
        return position - 1

    def process_tile(self, player, current_tile_index):
        """Makes appropriate changes to position, coin count, or crown count depending on what space a player lands on
        Args:
            player(str): Player whose turn it is.
            current_tile_index(int between 0-29): Tile player is currently on.
        Returns:
            current_tile(int between 0-29): Tile player is currently on.
        Side effect:
            Updating dictionary that stores players balances.
            Updating dictionary that stores players crown points.
            Updating dictionary that stores player position.
            Prints message that corresponds with the space that the player lands on.
        """
        if board[current_tile_index] == "normal":
            self.coin_count[player] += 5
            print(f"{player} landed on a normal space and got 5 coins")
        elif board[current_tile_index] == "chance":
            chance_result = r.randrange(2)
            if chance_result == 0:
                coin_value_result = r.randrange(2)
                if coin_value_result == 0:
                    self.coin_count[player] += 3
                    print(f"{player} landed on a chance space and got 3 coins")
                else:
                    self.coin_count[player] += 7
                    print(f"{player} landed on a chance space and got 7 coins")
            else:
                space_value_result = r.randrange(2)
                if space_value_result == 0:
                    self.player_position[player] += 3
                    self.player_position[player] %= len(board)
                    print(f"{player} landed on a chance space and moved up 3 spaces")
                else:
                    self.player_position[player] += 5
                    self.player_position[player] %= len(board)
                    print(f"{player} landed on a chance space and moved up 5 spaces")
                print(f"{player} is now on space {self.player_position[player] + 1}")
        elif board[current_tile_index] == "downbad":
            downbad_result = r.randrange(2)
            if downbad_result == 0:
                coin_value_result = r.randrange(2)
                if coin_value_result == 0:
                    if self.coin_count[player] <= 5:
                        self.coin_count[player] = 0
                        print(f"{player} landed on a downbad space and lost all their coins")
                    else:
                        self.coin_count[player] -= 5
                        print(f"{player} landed on a downbad space and lost 5 coins")
                else:
                    if self.coin_count[player] <= 10:
                        self.coin_count[player] = 0
                        print(f"{player} landed on a downbad space and lost all their coins")
                    else:
                        self.coin_count[player] -= 10
                        print(f"{player} landed on a downbad space and lost 10 coins")
            else:
                space_value_result = r.randrange(2)
                if space_value_result == 0:
                    self.player_position[player] -= 3
                    self.player_position[player] %= len(board)
                    print(f"{player} landed on a downbad space and moved back 3 spaces")
                else:
                    self.player_position[player] -= 5
                    self.player_position[player] %= len(board)
                    print(f"{player} landed on a downbad space and moved back 5 spaces")
                print(f"{player} is now on space {self.player_position[player] + 1}")

        else:
            self.jackpot(player)
            print(f"{player} landed on a JACKPOT space and received a crown!")



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

    def rock_paper_scissors(self):
        """Runs a game of Rock Paper Scissors against the computer every 3 turns.

        Side Effects:
            Prints the rules of the game and the amount of coins the player will bet.
            Prints the outcome of the RPS game.
            Updates the player's coin amount based on outcome of RPS.
        """
        print("\nIt's time to make this more interesting by gambling in a game of Rock Paper Scissors!")
        print(
            "\nThe rules: Rock crushes Scissors. Scissors cuts Paper. Paper covers Rock. If you win, you will double "
            "your wager. But if you lose, those coins are gone forever!")
        print(
            "\nYou don't want to wager? Too Bad! 10 coins is the cost to play! There will be no penalty or reward in "
            "the event of a tie.")
        for player in self.players:
            if self.coin_count[player] == 0:
                print(f"Jeez man. You're extra downbad... looks like {player} can't even afford to play with their "
                  f"friends. Everyone should laugh at them.")
                continue
            print(f"\nTime to make your move, {player}")
            playerChoice = int(input("Choose: 1 (Rock), 2 (Paper), or 3 (Scissors): "))
            # if choice not made between 1-3 then input will be asked for again
            while playerChoice > 3 or playerChoice < 1:
                playerChoice = int(input("Please enter a valid input: "))
                # playerMove is assigned value based on playerChoice
            if playerChoice == 1:
                playerMove = "Rock"
            elif playerChoice == 2:
                playerMove = "Paper"
            else:
                playerMove = "Scissors"
            print(f"{player}'s choice is: " + playerMove)
            # range 1-3 as there are 3 moves and a random move will be chosen
            computerChoice = r.randint(1, 3)
            # computerMove is assigned value based on computerChoice
            if computerChoice == 1:
                computerMove = "Rock"
            elif computerChoice == 2:
                computerMove = "Paper"
            else:
                computerMove = "Scissors"
            print("The computer chooses: " + computerMove)
            if ((playerChoice == 1 and computerChoice == 2) or (playerChoice == 2 and computerChoice == 1)):
                print("Paper Wins!")
                winner = "Paper"
            elif ((playerChoice == 1 and computerChoice == 3) or (playerChoice == 3 and computerChoice == 1)):
                print("Rock Wins!")
                winner = "Rock"
            elif playerChoice == computerChoice:
                print("Tie!")
                winner = "Nobody"
            else:
                print("Scissors Wins!")
                winner = "Scissors"
            # winner assigned and printed out
            if winner == playerMove:
                if self.coin_count[player] < 10:
                    print(f"\nYou win! You will now be awarded {self.coin_count[player]} coins!")
                    self.coin_count[player] *= 2
                else:
                    self.coin_count[player] += 10
                    print("\nYou win! You will now be awarded 10 coins!")
            elif winner == "Nobody":
                print("\nIt's a tie! Breaking even is better than losing!")
            else:
                print("\nComputer wins! Wow... this is really embarrassing. Maybe you shouldn't gamble anymore because "
                    "this is rough to watch. Hand over those coins, loser!")
                if self.coin_count[player] < 10:
                    self.coin_count[player] = 0
                else:
                    self.coin_count[player] -= 10

    def jackpot(self, player):
        """Controls events of the jackpot tile
        Args:
            player(int between 0-2): Player whose turn it is.
        Side effect:
            Updating dictionary that stores players crown points.
        """
        self.crown_count[player] += 1

    def is_game_over(self, player, max_crown_points):
        """Checks if any of the players have the requirements for winning
        Args:
            player(str): Player whose turn it is.
            max_crown_points(int): the amount of crown points required to win.
        Side effect:
            Printing to the terminal a win message and who won
        """
        if self.crown_count[player] == max_crown_points:
            print(f"Congrats {player} has won!")
            return True
        else:
            return False
    
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

def parse_args(arglist):
    """Parse command-line arguments.

    Three required arguments (the names of three players).
    An argument of how many crown points are needed to win.

    Returns:
        namespace: a namespace with four attributes: name0, name1, and name2, all
        strings. Also the amount of crown points needed to win.
    """
    parser = ArgumentParser()
    parser.add_argument("name0", help="the first player's name")
    parser.add_argument("name1", help="the second player's name")
    parser.add_argument("name2", help="the third player's name")
    parser.add_argument("-win_condition", type=int, default=5, help="chosen amount of crown points needed to win")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    the_game = Game(args.name0, args.name1, args.name2, args.win_condition)
    round_counter = 1
    print(str(the_game))
    while the_game.play_round(round_counter):
        round_counter += 1
        print(str(the_game))