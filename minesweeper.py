import random


class Board:
    height = 10
    width = 10
    num_bombs = 10
    bombs = []
    clicked = []

    def __init__(self):
        self.bombs = [[False for i in range(self.height)] for j in range(self.width)]
        self.clicked = [[" " for i in range(self.height)] for j in range(self.width)]
        i = 0
        if(self.num_bombs <= self.height * self.width):
            while i < self.num_bombs:
                bomb_height = random.randint(0, self.height-1)
                bomb_width = random.randint(0, self.width-1)
                if(self.bombs[bomb_height][bomb_width]) is False:
                    self.bombs[bomb_height][bomb_width] = True
#                    self.clicked[bomb_height][bomb_width] = "B"
                    i += 1

    def __str__(self):
        ret = ""
        for i in range(self.height):
            ret += str(i)
            for j in range(self.width):
                ret += "|" + self.clicked[i][j]
                ret += " "
            ret += "\n"
        for j in range(3*self.width+2):
            ret += "-"
        ret += "\nX"
        for j in range(self.width):
            ret += "|" + str(j) + " "
        return ret

    def num_bombs_adjacent(self, input_height, input_width):
        count = 0
        for i in range(max(0, input_height-1), min(self.height, input_height+1)+1):  # +1 is because stop on range is non-inclusive
            for j in range(max(0, input_width-1), min(self.width, input_width+1)+1):
                if(self.bombs[i][j] and not(i == input_height and j == input_width)):
                    count += 1
        return count


b = Board()
num_clicks = 0
while(True):
    userInput = input('Enter a Minesweeper Square in the form RowColumn, eg 00\n' + b.__str__() + "\n")
    if(len(userInput) != 2):
        print("Please input exactly 2 characters\n")
    else:
        try:
            input_height = int(userInput[0])
            input_width = int(userInput[1])
        except ValueError:
            print("Please input only 0-9 for Row and Column")
    if(b.bombs[input_height][input_width]):
        for i in range(b.height):
            for j in range(b.width):
                if(b.bombs[i][j]):
                    b.clicked[i][j] = "B"
        userInput = input('You clicked on a bomb!\n' + b.__str__() + "\nY to Quit\n")
        if(userInput == "Y"):
            break
        else:
            print("Starting a new game:\n")
            b = Board()
    else:
        if(b.clicked[input_height][input_width] == " "):
            num_clicks += 1
        b.clicked[input_height][input_width] = str(b.num_bombs_adjacent(input_height, input_width))
        if(num_clicks == b.height * b.width - b.num_bombs):
            userInput = input('You win!\n' + b.__str__() + "\nY to Quit\n")
