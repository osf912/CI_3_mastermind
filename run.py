from random import randint

class Row:
    """
    A Row is a line in the game with a codepart ( a list of
    4 numbers (0-5) (6 colors in the origin game) and a response
    part, where the responses are 
        2 -> there is one code at the right position
        1 -> there is a correct code in the list, but not the right position
        0 -> no response
    """
    code_part = [0,0,0,0]
    response_part = [0,0,0,0]

def __init__(self, code):
    self.code_part = code
    self.response_part = [0,0,0,0]

class CodeRow(Row):
    """
    A CodeRow is the row with the code to find in the
    mastermind game. One code is a number from 0 to num.
    """

    def __init__(self):
        """
        num is the range of the code, number between 0 and num
        """
        rand_list = []
        for i in range(4):
            rand_list.append(randint(0,5))
        print(rand_list)
        Row.__init__(rand_list)
        self.response_part = [2,2,2,2]
    
    def printCodeRow(self):
        print("Code:   | X | X | X | X |")
    
code = CodeRow()
code.printCodeRow()