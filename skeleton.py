die = [1,2,3,4,5,6] #random.randint random.randrange
board = {
            0:"normal",
            1:"chance",
            2:"normal",
            3:"normal",
            4:"downbad",
            5:"normal",
            6:"normal",
            7:"normal",
            8:"chance",
            9:"normal",
            10:"normal",
            11:"normal",
            12:"downbad",
            13:"chance",
            14:"normal",
            15:"normal",
            16:"downbad",
            17:"downbad",
            18:"normal",
            19:"normal",
            20:"normal",
            21:"chance",
            22:"normal",
            23:"normal",
            24:"normal",
            25:"chance",
            26:"downbad",            
            27:"normal",
            28:"normal",
            29:"jackpot"
            }
class Game:
        """ A class to play the game.
            
        Attributes:
            path(textfile in UTF-8): reading the file for special spaces.
            name0(string): player 1's name.
            name1(string): player 2's name.
            name2(string): player 3's name.
        """
        def __init__(self, path, name0, name1, name2): #read in the file here
            """ Initilizes game objects.
            Args:
                path(textfile in UTF-8): reading the file for special spaces.
                name0(string): player 1's name.
                name1(string): player 2's name.
                name2(string): player 3's name.
            Side effect: 
                Read the file.
                Reassign attribute names  .         
            """
        def movement(self, player_index, die_index, current_tile):
            """Rolls the die and moves the player the appropriate amount of spaces.
            Args:
                player_index(int between 0-2): Player whose turn it is.
                die_index(int between 1-6): Players roll on the die.
                current_tile(int between 0-29): Tile player is currently on.
            Returns:
                current_tile(int between 0-29): Tile player is currently on.
            Side effect:
                Printing the players current tile.
            """
        def currency(self, player_index, current_tile): #dict to keep track of currency
            """Keeps track of how many tokens and crown points each player has
            Args:
                player_index(int between 0-2): Player whose turn it is.
                current_tile(int between 0-29): Tile player is currently on.
            Returns:
                current_tile(int between 0-29): Tile player is currently on.
            Side effect:
                Updating dictionary that stores players balances.
                Updating dictionary that stores players crown points.
            """
        def play_round(self):
            """Manages a single round in the game
            Side effect:
                Updates appropriate containers and variables
            """
        def special_space(self, current_tile, chance, downbad):
            """Controls events of special tiles
            Args:
                current_tile(int between 0-29): Tile player is currently on.
                chance(string): Random chance selection from file
                downbad(string): Random downbad selection from file
            Side effect:
                Printing the result of the randomized chance space 
                Printing the result of the randomized downbad space
            """
        def jackpot(self, player_index, current_tile):
            """Controls events of the jackpot tile
            Args:
                player_index(int between 0-2): Player whose turn it is.
                current_tile(int between 0-29): Tile player is currently on.
            Side effect: 
                Updating dictionary that stores players crown points.
            """
        def game_over(self):
            """Checks if any of the players have the requirements for winning
            Side effect:
                Printing to the terminal a win message and who won
            """
if __name__ == "__main__":
    the_game = Game(args.name0,args.name1,args.name2)
    the_game.play_round()