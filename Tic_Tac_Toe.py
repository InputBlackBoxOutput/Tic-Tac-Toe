# File containing GUI for Cross and Nut Game Application
# Built using python's tkinter module

# File Name:Tic_Tac_Toe.py
# Description:Provides graphical user interface (GUI) for Cross & Nut game
#
# Written by Rutuparn Pawar
# Created on 29 Sept 2019
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

# Modify below import to import only those modules which are needed

'''Project Note: Renaming the file with .pyw extension is not working '''
import os
import sys

from tkinter import *
import tkinter.messagebox as msgbox

from Compute import *


class GUI(Tk):
    def __init__(self, background, font_size):
        super().__init__()
        self.board = Tic_Tac_Toe()

        self.title("Cross & Nut")
        self.geometry("410x420")
        self.wm_resizable(width=False, height=False)
        # self.wm_iconbitmap('path') Add .ico file to path

        self.bkgnd = background
        self.configure(bg=background)
        self.font_size = font_size

        self.move = 'cross'   # Cross plays first
        self.bot = True       # Default: Game vs computer

    # Binding functions for menu bar
    def Vs_computer(self):
        self.board.clear_cross_nut()
        self.update_board()
        self.bot = True
        self.move = 'cross'
        self.board.winner_string = None
        self.status.configure(text="Developed by Rutuparn Pawar")
        # print('Beginning game vs computer')

    def Vs_player(self):
        self.board.clear_cross_nut()
        self.update_board()
        self.bot = False
        self.board.winner_string = None
        self.move = 'cross'
        # print('Beginning game vs person')

    def how_to_play(self):
        with open(os.path.join(sys.path[0], "help.txt"), "rt") as help_file:
            msgbox.showinfo('HOW TO PLAY', help_file.read())

    def about(self):
        with open(os.path.join(sys.path[0], "about.txt"), "r") as about_file:
            msgbox.showinfo('ABOUT', about_file.read())

    '''Fxn to build menu bar'''
    def menu_bar(self):
        self.menu = Menu(self)
        self.menu.add_command(label='One player', command=self.Vs_computer)
        self.menu.add_command(label='Two player', command=self.Vs_player)
        self.menu.add_command(label='How to play', command=self.how_to_play)
        self.menu.add_command(label='About', command=self.about)
        self.menu.add_command(label='Close', command=quit)
        self.config(menu=self.menu)

    '''Fxn to build label to display winner'''
    def heading_label(self, padding):
        self.win_label = Label(self, text="Let's play Tic Tac Toe!", font="lucida 16 bold", padx=padding,
                               pady=round(padding / 5))
        self.win_label.pack(side=TOP, fill=X)
        Label(self, bg=self.bkgnd).pack(side=TOP)

    # Helper functions for playing grid
    def update_board(self):
        each_button = 0
        for each_r in range(0, 3):
            for each_c in range(0, 3):
                new_text = self.board.grid_map[each_r][each_c]
                self.b_list[each_button].configure(text=new_text, font=f"calibri {self.font_size - 1} bold")
                each_button = each_button + 1

        # If there is no winner notify the user and begin the game again
        if self.board.cross_nut_map['empty'] not in self.board.grid_map[0]:
            if self.board.cross_nut_map['empty'] not in self.board.grid_map[1]:
                if self.board.cross_nut_map['empty'] not in self.board.grid_map[2]:
                    msgbox.showinfo('No winner', "Looks like there is no winner.")
                    self.board.clear_cross_nut()
                    self.update_board()


    '''Helper function for button_pressed function'''
    def toggle_move(self):
        if self.move == 'cross':
            self.move = 'nut'
        else:
            self.move = 'cross'

    def whose_move(self):
        if self.move == 'cross':
            return 'Nut'
        else:
            return'Cross'

    def button_pressed(self, button, x, y):
        # Don't do anything if there is a winner
        if self.board.winner_string is not None :
             return

        # Do something if there is no winner
        # print(f'Button {button} pressed')

        stat = self.board.place_cross_nut(x, y, self.move)
        # print(self.board.grid_map)

        if self.bot is False:
            if stat:
                self.update_board()
                self.board.winner_string = self.board.winner_check(self.move)
                self.status.configure(text=f"{self.whose_move()}'s turn ")
                self.toggle_move()

            if self.board.winner_string is not None:
                self.status.configure(text=self.board.winner_string)
                return

        else:
            self.board.bot_move()
            self.update_board()
            
            self.board.winner_string = self.board.winner_check('nut')
            if self.board.winner_string is not None:
                self.status.configure(text=self.board.winner_string)
                return
            
            self.board.winner_string = self.board.winner_check('cross')
            if self.board.winner_string is not None:
                self.status.configure(text=self.board.winner_string)
                return
            

    # Binding functions for playing grid
    def b0(self):
        self.button_pressed(0, 0, 0)
    def b1(self):
        self.button_pressed(1, 0, 1)
    def b2(self):
        self.button_pressed(2, 0, 2)
    def b3(self):
        self.button_pressed(3, 1, 0)
    def b4(self):
        self.button_pressed(4, 1, 1)
    def b5(self):
        self.button_pressed(5, 1, 2)
    def b6(self):
        self.button_pressed(6, 2, 0)
    def b7(self):
        self.button_pressed(7, 2, 1)
    def b8(self):
        self.button_pressed(8, 2, 2)

    '''Fxn to build playing grid'''
    def play_grid(self, padding):
        self.canvas = Canvas(self, bg=self.bkgnd)
        self.grid_map = Frame(self.canvas, bg='grey')
        self.canvas.pack(fill=BOTH)

        # Draw line after game has a winner (Not working!)
        # Looks like drawing on canvas does not get superimposed on button widget
        #self.canvas.create_line(0, 0, 1000, 1000, fill="red")

        # Generate 9 button widgets
        self.b_list = []
        for each in range(0, 9):
            self.b_list.append(
                Button(self.grid_map, text='  ', font=f"calibri {self.font_size} bold", padx=padding, pady=padding))

        # Place 9 button widgets in a grid
        each = 0
        for r in range(0, 3):
            for c in range(0, 3):
                self.b_list[each].grid(row=r, column=c)
                each = each + 1

        # Mapping buttons in grid to functions
        self.b_list[0].configure(command=self.b0)
        self.b_list[1].configure(command=self.b1)
        self.b_list[2].configure(command=self.b2)

        self.b_list[3].configure(command=self.b3)
        self.b_list[4].configure(command=self.b4)
        self.b_list[5].configure(command=self.b5)

        self.b_list[6].configure(command=self.b6)
        self.b_list[7].configure(command=self.b7)
        self.b_list[8].configure(command=self.b8)

        self.grid_map.pack(side=BOTTOM)

        self.update_board()

    '''Fxn to build status bar'''
    def status_bar(self, padding):
        self.status = Label(self, text="Developed by Rutuparn Pawar", font='calibri 12 normal', borderwidth=1,
                            relief=SUNKEN, anchor='s', pady=padding)
        self.status.pack(side=BOTTOM, fill=X)
        Label(self, bg=self.bkgnd).pack(side=BOTTOM)

# ////////////////////////////////////////////////////////////////////////////////////////////
if __name__ == "__main__":
    print("Please minimize this window.")
    window = GUI(background='grey', font_size=10)
    window.menu_bar()
    window.heading_label(padding=2)
    window.status_bar(padding=2)
    window.play_grid(padding=40)
    window.mainloop()
