#!/usr/bin/python3.8

from typing import List
import os
import time
import click
import threading


printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

board_height = 20
board_width = 20
snake_width = 3
empty_space = '.'
snake_body = '*'
speed_sec = 0.3


"""Initial informations about snake's position and direction"""

snake_segments = [[7,9], [8,9], [9,9], [10,9], [11,9]]
number_of_snake_segments = len(snake_segments)
current_movement_direction = "right"


# class Snake_Game:
    


def get_empty_board(width: int, height: int, fill: str):
    '''Builds empty board'''


    empty_board = [[fill for _ in range(width)] for _ in range(height)]
    return empty_board



def display_board(snake_segments):
    '''Displays game board with the snake in initial position'''


    board = get_empty_board(width=board_width, height=board_height, fill=empty_space)
    for x, y in snake_segments:
        board[y][x] = snake_body
    for x in board:
        print(*x, '\r')
    

    
def update_snake(direction: str):
    """Updates snakes coordinates based on the moving direction."""
 
    if direction == "down":
        movement = snake_segments[-1].copy()
        movement[1] = movement[1] + 1
        snake_segments.append(movement)
        del snake_segments[0]
    elif direction == "up":
        movement = snake_segments[-1].copy()
        movement[1] = movement[1] - 1
        snake_segments.append(movement)
        del snake_segments[0]
    elif direction == "right":
        movement = snake_segments[-1].copy()
        movement[0] = movement[0] + 1
        snake_segments.append(movement)
        del snake_segments[0]
    elif direction == "left":
        movement = snake_segments[0].copy()
        movement[0] = movement[0] - 1
        snake_segments.insert(0, movement)
        del snake_segments[-1]



def run_thread():
    '''Starts seconds thread work'''


    thre1 = threading.Thread(target=moves, daemon=True)
    thre1.start()



def check_colision():
    '''Checks if snake don't touches walls'''


    if snake_segments[0][0] == 0:
        os.system('clear')
        print("---YOU LOSE!---YOUR SCORE WAS: " + str(score)+ "---")
        exit()
    if snake_segments[0][1] == 0:
        os.system('clear')
        print("---YOU LOSE!---YOUR SCORE WAS: " + str(score)+ "---")
        exit()
    if snake_segments[number_of_snake_segments - 1][0] == board_height - 1:
        os.system('clear')
        print("---YOU LOSE!---YOUR SCORE WAS: " + str(score)+ "---")
        exit()
    if snake_segments[number_of_snake_segments - 1][1] == board_width - 1:
        os.system('clear')
        print("---YOU LOSE!---YOUR SCORE WAS: " + str(score)+ "---")
        exit()   
    
    

if __name__ == '__main__':
    
    

    '''Shows basic informations about the game'''
    
    os.system('clear')
    print("This is a little snake game. You can control the snake by your keybord arrows. Be careful! Don't touch the walls!")
    time.sleep(5)
    
    
    
    def moves():
        '''Changes arrows input to change in snake movement direction'''


        while True:
            key_input = click.getchar()
            global current_movement_direction 
            if key_input == '\x1b[D':
                current_movement_direction = "left"  
            elif key_input == '\x1b[C':
                current_movement_direction = "right"
            elif key_input == '\x1b[A':
                current_movement_direction = "up"
            elif key_input == '\x1b[B':
                current_movement_direction = "down"

    

    run_thread()
    


    '''Puting together whole functions defining game and creates output'''

    score = 5
    while True:
        check_colision()
        display_board(snake_segments)
        update_snake(current_movement_direction)
        print("YOUR SCORE: " + str(score))
        score = score + 2
        time.sleep(speed_sec)
        os.system('clear')

    
    

    
# def get_snake(starting_point: int):
    # starting_point = list(map(int, starting_point.split()))
    # first_coord = starting_point[0]
    # second_coord = starting_point[1]
    # snake_segments.append((first_coord, second_coord)) 
    



