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
        super().__init__(rand_list)
        self.response_part = [2,2,2,2]
    
    def print_CodeRow(self):
        print("Code:   | X | X | X | X |")
    
class TryRow(Row):
    """
    A TryRow is the try to find the code in the game
    """
    def __init__(self, try_num):
        super().__init__(self)
        self.try_num = try_num # Try number for print-method
    
    def check_range(self):
        """
        Check, if the Integers in the code_part list are in the code range (0-5)
        """
        for i in range(4):
            if ((self.code_part[i] >= 0) and (self.code_part[i] <= 5)):
                print(self.code_part[i])
                continue
            else:
                print("Integers have to be from 0 to 5")
                return False
            
        return True

    def get_try(self):
        """
        Ask a new try from the user
        """
        while(True):
            try_str = input("Enter try: (4 comma separated Numbers (0-5)): ")
            try_list = try_str.split(',')
            
            if (len(try_list) != 4):
                print("Please type exactly 4 code numbers: ")
                continue

            try:
                for i in range(len(try_list)):
                    try_list[i] = int(try_list[i])
                self.code_part = try_list # now the code_part list is a list of integers
            except:
                print("Please enter Integers from 0 to 5")
            else:
                if(self.check_range()): 
                    return True

    def get_response(self, response_part):
        self.response_part = response_part

    def print_TryRow(self):
        c = self.code_part
        r = self.response_part
        print(f"{self.try_num}      | {c[0]} | {c[1]} | {c[2]} | {c[3]}  ||  {r[0]} | {r[1]} | {r[2]} | {r[3]}")

get_try_list = TryRow(10)
gt = get_try_list.get_try()
print(gt, get_try_list.code_part)