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
    mastermind game. One code is a number from 0 to 5.
    """

    def __init__(self):
        """
        Fill self.code_part with random number from 0 to 5.
        """
        rand_list = []
        for i in range(4):
            rand_list.append(randint(0,5))
        Row.__init__(rand_list)
        self.response_part = [2,2,2,2]
    
    def print_CodeRow(self):
        print("Code:   | X | X | X | X |")
    
class TryRow(Row):
    """
    A TryRow is the try to find the code in the game
    """
    def __init__(self, try_num):
        super().__init__(self, [0, 0, 0, 0])
        self.try_num = try_num # Try Number for print-method

    def getTry():
        """
        Ask the new try from the user
        """
        try = input("Enter try: (4 comma separated Numbers (0-5)")
        check_try(try)

        return try

    def check_try(try).

    def get_response(self, response_part):
        self.response_part = response_part

    def print_TryRow():
        c = self.code_part
        r = self.response_part
        print(f"{self.try_num}      | {c[0]} | {c[1]} | {c[2]} | {c[3]}  ||  {r[0]} | {r[1]} | {r[2]} | {r[3]}")

code = CodeRow()
code.print_CodeRow()

try = TryRow()
try.getTr