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
    __code_part = [0,0,0,0]
    __response_part = [0,0,0,0]

    def __init__(self, code):
        self.code_part = code
        self.response_part = [0,0,0,0]


    def get_code_part(self):
        return self.__code_part
    
    def set_code_part(self, code_list):
        self.__code_part = code_list

    def get_response_part(self):
        return self.__response_part
    
    def set_response_part(self, response_list):
        self.__response_part = response_list
    

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
    
    def print_covered(self):
        print("Code:   | X | X | X | X |")
    
    def print_solved(self):
        cr = self.code_part
        print(f"Code:   | {cr[0]} | {cr[1]} | {cr[2]} | {cr[3]} |")
    
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
        cp = self.get_code_part()
        for i in range(4):
            if ((cp[i] >= 0) and (cp[i] <= 5)):
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
                self.set_code_part(try_list) # now the code_part list is a list of integers
            except:
                print("Please enter Integers from 0 to 5")
            else:
                if(self.check_range()): 
                    return True

    def get_response(self, response_part):
        self.set_response_part(response_part)

    def print_try(self):
        c = self.get_code_part()
        r = self.get_response_part()
        try_num_str = str(self.try_num)
        if (self.try_num < 10):
            try_num_str = " " + try_num_str
            
        print(f"{try_num_str}      | {c[0]} | {c[1]} | {c[2]} | {c[3]} | | {r[0]} | {r[1]} | {r[2]} | {r[3]} |")

# class MastermindGame:




cr = CodeRow()
cr.print_covered()
cr.print_solved()

get_try_list = TryRow(8)
gt = get_try_list.get_try()
get_try_list.print_try()