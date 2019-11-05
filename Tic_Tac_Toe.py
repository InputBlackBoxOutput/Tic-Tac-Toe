# File containing algorithm for Cross and Nut Game Application
# Built using python's tkinter module

# File Name:Tic_Tac_Toe.py
# Description:Provides game algorithm for Cross & Nut game
#
# Written by Rutuparn Pawar
# Created on 5 Sept 2019
#
# Software License Agreement:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import random  # Used by Game_Bot Class


class Tic_Tac_Toe:

    def __init__(self):
        # self.grid_map = [['O', 'X', 'X'], ['O', 'X', 'O'], ['O', 'O', 'O']]  # Use for testing purpose
        self.grid_map = [['  ', '  ', '  '], ['  ', '  ', '  '], ['  ', '  ', '  ']]
        self.cross_nut_map = {'cross': 'X', 'empty': '  ', 'nut': 'O'}
        self.winner_string = None

    """Function to place cross/nut in grid if place is empty"""

    def place_cross_nut(self, x, y, place):
        if place == 'cross':
            if self.grid_map[x][y] == '  ':
                self.grid_map[x][y] = self.cross_nut_map[place]
                return f'Cross placed at ({x},{y})'
            else:
                return f'Cross cannot be placed at ({x},{y}) since place is not empty'
        elif place == 'nut':
            if self.grid_map[x][y] == '  ':
                self.grid_map[x][y] = self.cross_nut_map[place]
                return f'Nut placed at ({x},{y})'
            else:
                return f'Nut cannot be placed at ({x},{y}) since place is not empty'
        else:
            self.grid_map[x][y] = self.cross_nut_map['empty']

    """Function to check if the player/computer has won"""

    def winner_check(self, player):

        # Check for 3 cross/nut in a row
        for x in range(0, 3):
            win_count = 0
            for y in range(0, 3):
                if self.cross_nut_map[player] == self.grid_map[x][y]:
                    win_count = win_count + 1
            if win_count == 3:
                print('Complete Row', end='\n\n')
                return 'Winner is ' + player

        # Check for 3 cross/nut in a column
        for y in range(0, 3):
            win_count = 0
            for x in range(0, 3):
                if self.cross_nut_map[player] == self.grid_map[x][y]:
                    win_count = win_count + 1
            if win_count == 3:
                print('Complete column', end='\n\n')
                return 'Winner is ' + player

                # Check for 3 cross/nut across diagonals

        win_count = 0
        for i in range(0, 3):
            if self.cross_nut_map[player] == self.grid_map[i][i]:
                win_count = win_count + 1
        if win_count == 3:
            print('Complete Diagonal \\', end='\n\n')
            return 'Winner is ' + player

        win_count = 0
        for i in range(2, -1, -1):
            if self.cross_nut_map[player] == self.grid_map[i][i]:
                win_count = win_count + 1
        if win_count == 3:
            print('Complete Diagonal /', end='\n\n')
            return 'Winner is ' + player

        return None

    '''Function to clear grid_map'''
    def clear_cross_nut(self):
        for each_r in range(0, 3):
            for each_c in range(0, 3):
                self.grid_map[each_r][each_c] = self.cross_nut_map['empty']

    """ Function to display grid on console for testing """
    def display_for_testing(self):
        index = [0, 1, 2]
        for x in index:
            for y in index:
                print(self.grid_map[x][y], end=' ')
            print()

    """ Function to run gameloop in console for testing """

    def gameloop_for_testing(self):

        print("CROSS & NUT")
        print('Important Note - !!!!! GRID MAY BEEN PREDEFINED !!!!!')

        while self.winner_string is None:

            self.display_for_testing()
            print("Player X")
            x = input("Enter x coordinate :")
            y = input("Enter y coordinate :")
            self.place_cross_nut(int(x), int(y), 'cross')
            self.winner_string = self.winner_check('cross')

            if self.winner_string is not None:
                break

            self.display_for_testing()

            print("Player O")
            x = input("Enter x coordinate :")
            y = input("Enter y coordinate :")
            self.place_cross_nut(int(x), int(y), 'nut')
            self.winner_string = self.winner_check('nut')

        self.display_for_testing()
        print(self.winner_string)

        return

    # Player is always cross hence begins the game

    """"Function to generate random unoccupied position"""

    def random_position(self):
        position = [-1, -1]
        found_position = True

        retries =0
        while (found_position):
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if self.grid_map[x][y] == self.cross_nut_map['empty']:
                position[0] = x
                position[1] = y
                found_position = False

            retries = retries + 1
            if retries == 10:
                print("Error: random_position tries exceeded")
                break

        return position

    """Function to get computer's move in a game vs computer"""

    def bot_move(self):

        # For manual difficulty setting (Not used)
        # if difficulty == 'hard':
        #     max_retries = 5
        # elif difficulty == 'easy':
        #     max_retries = 1
        # else:
        #     max_retries = 2

        # Difficulty increased by increasing the number of retries
        run = random.randint(1, 7)
        print(f"Difficulty = {run}")

        while run is not 0:
            print(f'Pass ({run})')

            position = self.random_position()
            print(position)

            self.grid_map[position[0]][position[1]] = self.cross_nut_map['nut']

            print(self.grid_map)

            win = self.winner_check('nut')

            if win is None:
                self.grid_map[position[0]][position[1]] = self.cross_nut_map['empty']
            else:
                self.place_cross_nut(position[0], position[1], 'nut')
                break

            run = run - 1
            if run is 0:
                position = self.random_position()
                print(f"Finally {position}")
                self.place_cross_nut(position[0], position[1], 'nut')
                print(self.grid_map)



# For testing game vs person
# game=Tic_Tac_Toe()
# game.gameloop_for_testing()

# For testing game vs computer
# bot = Game_Bot()
# bot.display_for_testing()
# bot.bot_move()
# bot.display_for_testing()