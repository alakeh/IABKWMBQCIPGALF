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