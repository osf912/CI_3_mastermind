"""
A Mastermind game: You have to find a fourdigit code, every number is
between 0 and five. The computer gives you a response to your input.
Responses are:
        2 -> there is one code at the right position
        1 -> there is a correct code in the list, but not at the right
                position
        0 -> no response
The response is as well a fourdigit code, but the response is not
necesarily at the corresponding position. First the 2's, than the 1's,
than trailling zeros.
"""
from random import randint


class Row:
    """
    A Row is a line in the game with a codepart and a response part.
    """
    def __init__(self, code):
        """
        Initiate Row with the given code
        """
        self.__code_part = code
        self.__response_part = [0, 0, 0, 0]

    def get_code_part(self):
        """
        Getter for __code_part
        """
        return self.__code_part

    def set_code_part(self, code_list):
        """
        Setter for __code_part
        """
        self.__code_part = code_list

    def get_response_part(self):
        """
        Getter for __response_part
        """
        return self.__response_part

    def set_response_part(self, response_list):
        """
        Setter for __response_part
        """
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
            rand_list.append(randint(0, 5))
        super().__init__(rand_list)
        self.set_response_part([2, 2, 2, 2])

    def print_covered(self):
        """
        Print the covered Codeline to the terminal
        """
        print("Code:   | X | X | X | X | |    Response   |")

    def print_solved(self):
        """
        Print the uncovered Codeline to the terminal
        """
        cr = self.get_code_part()
        print(f"Code:   | {cr[0]} | {cr[1]} | {cr[2]} | {cr[3]} |")

    def new_code(self):
        """
        Add a new code to the CodeRow for a new game
        """
        rand_list = []
        for i in range(4):
            rand_list.append(randint(0, 5))
        self.set_code_part(rand_list)


class TryRow(Row):
    """
    A TryRow is the try to find the code in the game
    """
    def __init__(self, try_num):
        """
        Initiate TryRow wih given trynumber
        """
        super().__init__([0, 0, 0, 0])
        self.try_num = try_num    # Try number for print-method

    def __check_range(self):
        """
        Check, if the Integers in the code_part list are in the
        code range (0-5) | private method
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
        Ask a new try from the user and check for correct type, count and range
        """
        while True:
            try_str = input("Enter try: (4 comma separated Numbers (0-5)): ")
            try_list = try_str.split(',')

            if len(try_list) != 4:
                print("Please type exactly 4 code numbers: ")
                continue

            try:
                for i in range(len(try_list)):
                    try_list[i] = int(try_list[i])
                self.set_code_part(try_list)
            except ValueError:
                print("Please enter Integers from 0 to 5")
            else:
                if self.__check_range():
                    return True

    def print_try(self):
        """
        Print the game row to the terminal
        """
        c = self.get_code_part()
        r = self.get_response_part()
        try_num_str = str(self.try_num)
        if self.try_num < 10:
            try_num_str = " " + try_num_str

        print(f"{try_num_str}      | {c[0]} | {c[1]} | {c[2]} | {c[3]} |" +
              f" | {r[0]} | {r[1]} | {r[2]} | {r[3]} |")


class MastermindGame:
    """
    The game class itself. Initialize game board, order the processes and
    give feedback to the tries.
    """

    def __init__(self):
        """
        The game board is a CodeRow (covered) and 12 tries. The 13. Row is the
        solution of the code, so a CodeRow (solved)
        """
        self.__board = []
        self.__solved_counter = 0
        cr = CodeRow()
        self.__board.append(cr)
        for i in range(1, 13):
            self.__board.append(TryRow(i))
        self.__board.append(cr)

    def print_board(self, num):
        """
        Print board from start to row num
        """
        print("-------------------------------------------")
        self.get_board(0).print_covered()
        if (num > 0) and (num <= 13):
            for i in range(1, num):
                self.get_board(i).print_try()
        else:
            for i in range(1, 13):
                self.get_board(i).print_try()
            self.get_board(13).print_solved()
            print("-------------------------------------------")

    def calculate_response(self, try_num):
        """
        Calculate game response: Add a 2 for every correct number
        on correct position. Add a 1 for the right number, but on
        the wrong position. Fill to len(4) with trailing zeros.
        """
        response = []
        pop_list = []

        # copy lists code and trial to not change the originals
        code = []
        trial = []
        code.extend(self.get_board(0).get_code_part())
        trial.extend(self.get_board(try_num).get_code_part())

        # check for right code on right position
        for i in range(4):
            if code[i] == trial[i]:
                pop_list.append(i)
                response.append(2)

        # delete them from the lists
        for i in reversed(pop_list):
            code.pop(i)
            trial.pop(i)
        pop_list = []

        # code & try are empty -> you won, otherwise check on
        # right code at wrong position
        if code != []:
            i = j = len(code)-1
            while i >= 0:
                while j >= 0:
                    if code[i] == trial[j]:
                        response.append(1)
                        code.pop(i)
                        trial.pop(j)
                        i = j = len(code)-1
                    else:
                        j -= 1
                i -= 1
                j = len(code)-1
        else:
            self.get_board(try_num).set_response_part(response)

        # add trailing zeros if list is shorter
        if len(response) < 4:
            for i in range(4 - len(response)):
                response.append(0)
        self.get_board(try_num).set_response_part(response)

    def clear_board(self):
        """
        Clear the board for the next round to play
        """
        for i in range(14):
            self.__board[i].set_code_part([0, 0, 0, 0])
            self.__board[i].set_response_part([0, 0, 0, 0])

    def inc_solved_counter(self):
        """
        Increment counter for solved Games in one session
        """
        self.__solved_counter += 1

    def get_solved_counter(self):
        """
        Getter for __solved_counter
        """
        return self.__solved_counter

    def get_board(self, num):
        """
        Getter for __board row num, if num is out of range,
        return the whole __board
        """
        if (num >= 0 and num <= len(self.__board)):
            return self.__board[num]
        else:
            return self.__board


def main():
    """
    Playing the game...
    """
    no_end = True

    while no_end:
        mmg = MastermindGame()
        for i in range(1, 13):
            mmg.print_board(i)
            mmg.get_board(i).get_try()
            mmg.calculate_response(i)
            mmg.get_board(i).print_try()
            if (mmg.get_board(i).get_response_part() == [2, 2, 2, 2]):
                print("-------------------------------------------")
                print("                You won!                   ")
                print("-------------------------------------------")
                print("\n")
                mmg.inc_solved_counter()
                break
        print(f"you have solved {mmg.get_solved_counter()}" +
              " games in this session.")
        again = input("Do you want to play another one..? (y/n)  ")
        try:
            if again.lower() != 'y':
                no_end = False
        except TypeError:
            print("Please insert just a character ('y' or 'n').")
            no_end = False


main()
