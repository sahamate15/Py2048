# Py2048
# Play 2048 in your python terminal!

# Shubham Sahamate
# Project Start Date: Monday, 20 July 2020

# Defining the core game class

import os, sys, time
import numpy as np
import random

class Py2048:
    '''
    The logic that runs the game
    '''
    def __init__(self):
        self.nums_matrix = np.zeros((4,4))
        self.error = False
        self.win_cond = False
        self.move_count = 0
        self.rand_num_alloc()
        self.rand_num_alloc()

    def action_handler(self, user_input):
        '''
        Handles the action to be taken after taking input from user
        movement_matrix is used to create the movement loops
        '''
        self.user_input = user_input
        temp_matrix = self.nums_matrix.copy()
        itr_range = 1

        def equality_check(matrix1, matrix2):
            '''
            Checks if two matrices (numpy arrays) are equal
            Equality is True for all values being equal
            '''
            for i in range(4):
                for j in range(4):
                    if matrix1[i][j] != matrix2[i][j]:
                        self.error = True
            else:
                self.error = False
                self.rand_num_alloc()
                self.move_count += 1

        def up_mvmt(self):
            '''
            Creates the up movement
            '''
            for itr in range(itr_range):
                for i in range(4):
                    for j in range(4):
                        selection = self.nums_matrix[i][j]
                        if i-1 > -1 and self.nums_matrix[i-1][j] == 0:
                            self.nums_matrix[i-1][j] = selection
                            self.nums_matrix[i][j] = 0
                        elif i-1 > -1 and self.nums_matrix[i-1][j] == selection:
                            self.nums_matrix[i-1][j] = selection*2
                            self.nums_matrix[i][j] = 0
                        else:
                            continue

        def left_mvmt(self):
            '''
            Creates the left movement
            '''
            for itr in range(itr_range):
                for i in range(4):
                    for j in range(4):
                        selection = self.nums_matrix[i][j]
                        if j-1 > -1 and self.nums_matrix[i][j-1] == 0:
                            self.nums_matrix[i][j-1] = selection
                            self.nums_matrix[i][j] = 0
                        elif j-1 > -1 and self.nums_matrix[i][j-1] == selection:
                            self.nums_matrix[i][j-1] = selection*2
                            self.nums_matrix[i][j] = 0
                        else:
                            continue

        def down_mvmt(self):
            '''
            Creates the down movement
            '''
            for itr in range(itr_range):
                for i in range(4):
                    for j in range(4):
                        selection = self.nums_matrix[i][j]
                        if i+1 < 4 and self.nums_matrix[i+1][j] == 0:
                            self.nums_matrix[i+1][j] = selection
                            self.nums_matrix[i][j] = 0
                        elif i+1 < 4 and self.nums_matrix[i+1][j] == selection:
                            self.nums_matrix[i+1][j] = selection*2
                            self.nums_matrix[i][j] = 0
                        else:
                            continue

        def right_mvmt(self):
            '''
            Creates the right movement
            '''
            for itr in range(itr_range):
                for i in range(4):
                    for j in range(4):
                        selection = self.nums_matrix[i][j]
                        if j+1 < 4 and self.nums_matrix[i][j+1] == 0:
                            self.nums_matrix[i][j+1] = selection
                            self.nums_matrix[i][j] = 0
                        elif j+1 < 4 and self.nums_matrix[i][j+1] == selection:
                            self.nums_matrix[i][j+1] = selection*2
                            self.nums_matrix[i][j] = 0
                        else:
                            continue

        if self.user_input == 'q':
            self.error = False
            sys.exit()

        elif self.user_input == 'n':
            self.error = False
            self.__init__()

        elif self.user_input == 'w':
            self.error = False
            up_mvmt(self)
            equality_check(temp_matrix, self.nums_matrix)

        elif self.user_input == 'a':
            self.error = False
            left_mvmt(self)
            equality_check(temp_matrix, self.nums_matrix)

        elif self.user_input == 's':
            self.error = False
            down_mvmt(self)
            equality_check(temp_matrix, self.nums_matrix)

        elif self.user_input == 'd':
            # LEFT movement action
            self.error = False
            right_mvmt(self)
            equality_check(temp_matrix, self.nums_matrix)

        else:
            self.error = True
            print('Error! Try again')

    def rand_num_alloc(self):
        '''
        Generates and allocates a random location to either 2 or 4
        '''
        allocation = False
        while allocation == False:
            x,y = np.random.choice([0, 1, 2, 3], size=(2,))
            if self.nums_matrix[x][y] == 0:
                if self.move_count > 6:
                    self.nums_matrix[x][y] = np.random.choice([2,4])
                    allocation = True
                    break
                else:
                    self.nums_matrix[x][y] = 2
                    allocation = True
                    break
            else:
                continue
