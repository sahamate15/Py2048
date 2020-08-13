# Terminal 2048
# Play 2048 in your terminal!

# Shubham Sahamate
# Project Start Date: Monday, 20 July 2020

# Executing the game

import os, sys, time
import numpy as np
import random
from Py2048 import Py2048

WIDTH, HEIGHT = (36, 14)
LEFT_PADDING = ' '*4
TOP_PADDING = '\n'*1
BOTTOM_PADDING = '\n'*2

def clear_screen():
    '''
    Clears the screen for each event refresh cycle
    Cross-platform for both windows and unix systems (Mac OS/Linux/etc)
    '''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def box_generator(nums_matrix):
    '''
    Prints the various boxes as seen in the console/terminal
    '''
    inner_box_top_lines = [k+1 for k  in range(0,11,3)]
    inner_box_edge_lines = [k+2 for k in range(0,11,3)]
    inner_box_bottom_lines = [k+3 for k in range(0,11,3)]
    left_up, right_up = ('╔', '╗')
    left_down, right_down = ('╚', '╝')
    sidewall, innerline = ('║', '═')
    matrix_row = 0

    for line_num in range(HEIGHT):
        if line_num == 0:
            # top line of big box
            print(''.join((LEFT_PADDING, left_up,
            innerline*(WIDTH-2), right_up)))
        elif line_num in inner_box_top_lines:
            # top lines of inner boxes
            print(''.join((LEFT_PADDING, sidewall, ' ',
            ''.join((left_up, innerline*6, right_up))*4, ' ', sidewall)))
        elif line_num in inner_box_edge_lines:
            # middle line of inner boxes
            # holds the numbers of the game
            temp_nums = nums_matrix[matrix_row]
            temp_nums_2 = []
            for num in temp_nums:
                if int(num) == 0:
                    temp_nums_2.append(' ')
                else:
                    temp_nums_2.append(int(num))
            box_nums = []

            def int_len(num):
                '''
                Checks the length of an integer
                '''
                if type(num) == int:
                    return len(str(num))
                else:
                    return 1

            for num in temp_nums_2:
                if int_len(num) == 1:
                    box_nums.append(''.join((' '*3, str(num), ' '*2)))
                elif int_len(num) == 2:
                    box_nums.append(''.join((' '*2, str(num), ' '*2)))
                elif int_len(num) == 3:
                    box_nums.append(''.join((' '*2, str(num), ' ')))
                elif int_len(num) == 4:
                    box_nums.append(''.join((' ', str(num), ' ')))
            print(''.join((LEFT_PADDING, sidewall, ' ', sidewall,
                       box_nums[0], sidewall, sidewall,
                       box_nums[1], sidewall, sidewall,
                       box_nums[2], sidewall, sidewall,
                       box_nums[3], sidewall, ' ', sidewall)))
            matrix_row += 1
        elif line_num in inner_box_bottom_lines:
            # bottom line of inner boxes
            print(''.join((LEFT_PADDING, sidewall, ' ',
            ''.join((left_down, innerline*6, right_down))*4, ' ', sidewall)))
        elif line_num == (HEIGHT-1):
            # lowest line of big box
            print(''.join((LEFT_PADDING, left_down,
            innerline*(WIDTH-2), right_down)))


def center_text(text):
    '''
    text -> the input string to be printed
    WIDTH -> the width of the box in question

    Prints the text at the center approximate center of the box,
    whether it is outer big box or inner small box
    '''
    padding_left, padding_right = (0, 0)
    if len(text) % 2 == 0:
        padding_left = (WIDTH - len(text))/2
        return (''.join((LEFT_PADDING,' '*int(padding_left), text,
                ' '*int(padding_right))))
    else:
        padding_left = (WIDTH - len(text)+1)/2
        return (''.join((LEFT_PADDING, ' '*int(padding_left), text,
                ' '*int(padding_right))))

def show_game(error, nums_matrix, win_cond):
    '''
    Displays the play area in terminal/console
    error -> Boolean, decides whether to print error message or not
    num_matrix -> Array of numbers to be shown on screen
    '''
    clear_screen()
    INSTRUCTIONS = ' '.join(('w:↑', 'a:←', 's:↓', 'd:→'))
    print(TOP_PADDING)
    print(center_text('2048 in Python Console'))
    box_generator(nums_matrix)
    print(center_text(INSTRUCTIONS))
    print(center_text('Enter/Return to Execute'))
    print(center_text('n: new game'))
    print(center_text('q: quit'))
    # Handling improper keyboard inputs
    if error == False and win_cond == False :
        print('\n\n')
    elif error == True:
        print('\n')
        print(center_text('Error! Improper Input! Try Again'))
    # Handling Victory
    if win_cond == True:
        print('\n')
        print(center_text('You Won! Continue or Start Over'))

def cls_countdown():
    '''
    Creates a 5 second countdown before screen is cleared
    and the game is started
    '''
    print('\nWelcome to Terminal 2048!\n')
    print('Clearing screen in...\n')
    for i in range(5)[::-1]:
        print(i+1)
        time.sleep(0.75)

def win_check(nums_matrix):
    '''
    Checks if the user has won
    '''
    for i in range(4):
        for j in range(4):
            if nums_matrix[i][j] == 2048:
                return True
                Break
    else:
        return False

def main():
    '''
    Runs the show
    '''
    cls_countdown()
    os.system('title Py2048')
    game = Py2048()
    while True:
        game.win_cond = win_check(game.nums_matrix)
        show_game(game.error, game.nums_matrix, game.win_cond)
        print(center_text(' '.join((str(game.move_count), 'MOVES'))))
        # print(center_text(' '.join((str(score_counter(game.nums_matrix)), 'POINTS'))))
        user_input = input((center_text('ACTION: '))).lower()
        game.action_handler(user_input)

if __name__ == '__main__':
    main()
