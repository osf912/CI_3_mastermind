from random import randint

class Row:
    """
    A Row is a line in the game with a codepart (a list of
    4 numbers (0-5) (6 colors in the origin game) and a response
    part, where the responses are 
        2 -> there is one code at the right position
        1 -> there is a correct code in the list, but not the right position
        0 -> no response
    """
    __code_part = [0,0,0,0]
    __response_part = [0,0,0,0]

    def __init__(self, code):
        self.__code_part = code
        self.__response_part = [0,0,0,0]

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

    def new_code(self):
        rand_list = []
        for i in range(4):
            rand_list.append(randint(0,5))
        self.set_code_part(rand_list)
    
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

    def print_try(self):
        c = self.get_code_part()
        r = self.get_response_part()
        try_num_str = str(self.try_num)
        if (self.try_num < 10):
            try_num_str = " " + try_num_str
            
        print(f"{try_num_str}      | {c[0]} | {c[1]} | {c[2]} | {c[3]} | | {r[0]} | {r[1]} | {r[2]} | {r[3]} |")

class MastermindGame:
    """
    The game class itself. Initialize game board, order the processes and give feedback to the tries. 
    """
    __board = []
    __solved_counter = 0

    def __init__(self):
        """
        The game board is a CodeRow (covered) and 12 tries. The 13. Row is the solution of the code, so a
        CodeRow (solved)
        """
        cr = CodeRow()
        self.__board.append(cr)
        for i in range(1,13):
            self.__board.append(TryRow(i))
        self.__board.append(cr)
    
    def print_board(self, num):
        print("-----------------------------------")
        self.get_board(0).print_covered()
        if (num > 0) and (num <= 12):
            for i in range(1,num):
                self.get_board(i).print_try()
        else:
            for i in range(1,13):
                self.get_board(i).print_try()
            self.get_board(13).print_solved()
            print("-----------------------------------")

    def calculate_response(self, try_num):
        code = self.__board[0].get_code_part()
        trial = self.__board[try_num].get_code_part()
        response = []
        pop_list = []

        # check for right code on right position
        for i in range(4):
            if (code[i] == trial[i]):
                pop_list.append(i)
                response.append(2)

        # delete them from the lists
        for i in range(len(pop_list)):
            code.pop(i)
            trial.pop(i)
        pop_list = []

        # code & try are empty -> you won, otherwise check on right code at wrong position
        if code != []:
            for i in range(len(code)):
                for j in range(len(code)):
                    if (code[i] == trial[j]):
                        response.append(1)

        # add trailing zeros
        if (len(response) != 4):
            for i in range(3 - len(response)):
                response.append(0)

        self.__board[try_num].set_response_part(response)

    def clear_board(self):
        for i in range(14):
            self.__board[i].set_code_part([0,0,0,0])
            self.__board[i].set_response_part([0,0,0,0])
    
    def inc_solved_counter(self):
        __solved_counter += 1
    
    def get_solved_counter(self):
        return self.__solved_counter

    def get_board(self,num):
        if (num>=0 and num<=len(self.__board)):
            return self.__board[num]
        else:
            return self.board

def main():
    mmg = MastermindGame()
    for i in range(1,14):   
        mmg.get_board(i).get_try()
        mmg.calculate_response(i)
        mmg.print_board(i)
        if mmg.get_board(i).get_response() == [2,2,2,2]:
            print("-----------------------------------")
            print("            You won!               ")
            print("-----------------------------------")
            mmg.inc_solved_counter()
            break
    print("end")

# main()

row = Row([5,0,5,0])
row.set_code_part([4,3,2,1])
row.set_response_part([2,2,1,0])
print(row.get_code_part())
print(row.get_response_part())
