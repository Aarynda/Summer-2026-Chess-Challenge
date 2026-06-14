import sys
import pathlib
import os

valid_moves = {}

class move:
    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos
        self.end_pos = end_pos

#default board assuming player plays as white
board = [
    ["Rb", "Nb", "Bb", "Qb", "Kb", "Bb", "Nb", "Rb"],
    ["pb", "pb", "pb", "pb", "pb", "pb", "pb", "pb"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["pw", "pw", "pw", "pw", "pw", "pw", "pw", "pw"],
    ["Rw", "Nw", "Bw", "Qw", "Kw", "Bw", "Nw", "Rw"]
]

player = "white"

piece_to_char = {
    "Rb" : "\u265C",
    "Nb" : "\u265E",
    "Bb" : "\u265D",
    "Qb" : "\u265B",
    "Kb" : "\u265A",
    "pb" : "\u265F",
    "Rw" : "\u2656",
    "Nw" : "\u2658",
    "Bw" : "\u2657",
    "Qw" : "\u2655",
    "Kw" : "\u2654",
    "pw" : "\u2659",
    "" : " "
}

FEN_to_my_notation = {
    "r" : "Rb",
    "n" : "Nb",
    "b" : "Bb",
    "q" : "Qb",
    "k" : "Kb",
    "p" : "pb",
    "R" : "Rw",
    "N" : "Nw",
    "B" : "Bw",
    "Q" : "Qw",
    "K" : "Kw",
    "P" : "pw"
}

def render_board(board):
    os.system("cls")
    for i in range(0, 8):
        print_string = " "
        for j in range(0, 8):
            print_string += piece_to_char[board[i][j]]
            if j != 7:
                print_string += " | "
        print(print_string)
        if i != 7:
            print("-------------------------------")

def print_intro():
    print("Welcome to chess!")

def generate_valid_moves():
    global valid_moves
    valid_moves = {}
    if(player == "white"):
        for i in range(0, 8):
            for j in range(0, 8):
                if(len(board[i][j]) > 1 and board[i][j][-1] == 'w'):
                    piece = board[i][j][0]
                    match piece:
                        #pawn
                        case 'p':
                            #move forward one space
                            if(board[i - 1][j] == ""):
                                rank = 8 - (i - 1)
                                file = chr(j + 0x61)
                                valid_moves[f"{file}{rank}"] = move((i, j), (i - 1, j))
                            #move forward two spaces
                            if(i == 6 and board[i - 2][j] == "" and board[i - 1][j] == ""):
                                rank = 8 - (i - 2)
                                file = chr(j + 0x61)
                                valid_moves[f"{file}{rank}"] = move((i, j), (i - 2, j))
                            #capture diagonal
                            if(j > 0 and i > 0 and board[i - 1][j - 1] != "" and board[i - 1][j - 1][-1] == "b"):
                                rank = 8 - (i - 1)
                                file = chr(j - 1 + 0x61)
                                valid_moves[f"{file}{rank}"] = move((i, j), (i - 1, j - 1))
                            if(j < 7 and i > 0 and board[i - 1][j + 1] != "" and board[i - 1][j + 1][-1] == "b"):
                                rank = 8 - (i - 1)
                                file = chr(j + 1 + 0x61)
                                valid_moves[f"{file}{rank}"] = move((i, j), (i - 1, j + 1))
                        case 'R':
                            for l in range(0, 8):
                                if(l < i):
                                    move_valid = True
                                    for m in range(l + 1, i):
                                        if(board[m][j] != ""):
                                            move_valid = False
                                    if(board[l][j] != "" and board[l][j][-1] != "b"):
                                        move_valid = False
                                    if(move_valid):
                                        rank = 8 - l
                                        file = chr(j + 0x61)
                                        valid_moves[f"R{file}{rank}"] = move((i, j), (l, j))
                                elif(l > i):
                                    move_valid = True
                                    for m in range(i + 1, l + 1):
                                        if(board[m][j] != ""):
                                            move_valid = False
                                    if(board[l][j] != "" and board[l][j][-1] != "b"):
                                        move_valid = False
                                    if(move_valid):
                                        rank = 8 - l
                                        file = chr(j + 0x61)
                                        valid_moves[f"R{file}{rank}"] = move((i, j), (l, j))
                                else:
                                    continue
                            for l in range(0, 8):
                                if(l < j):
                                    move_valid = True
                                    for m in range(l + 1, j):
                                        if(board[i][m] != ""):
                                            move_valid = False
                                    if(board[i][l] != "" and board[i][l][-1] != "b"):
                                        move_valid = False
                                    if(move_valid):
                                        rank = 8 - i
                                        file = chr(l + 0x61)
                                        valid_moves[f"R{file}{rank}"] = move((i, j), (i, l))
                                elif(l > j):
                                    move_valid = True
                                    for m in range(j + 1, l + 1):
                                        if(board[i][m] != ""):
                                            move_valid = False
                                    if(board[i][l] != "" and board[i][l][-1] != "b"):
                                        move_valid = False
                                    if(move_valid):
                                        rank = 8 - i
                                        file = chr(l + 0x61)
                                        valid_moves[f"R{file}{rank}"] = move((i, j), (i, l))
                                else:
                                    continue

                        case _:
                            continue

def show_valid_moves():
    print(valid_moves.keys())

def game_terminal():
    game_continue = True
    global board
    while game_continue:
        command = input("> ")
        generate_valid_moves()
        match command:
            case "quit":
                game_continue = False
                print("Exiting game")
                return
            case "help":
                show_valid_moves()
            case _:
                if(command in valid_moves.keys()):
                   start_pos = valid_moves[command].start_pos
                   end_pos = valid_moves[command].end_pos
                   piece = board[start_pos[0]][start_pos[1]]
                   board[start_pos[0]][start_pos[1]] = ""
                   if(board[end_pos[0]][end_pos[1]] != ""):
                       print("Capture!")
                   board[end_pos[0]][end_pos[1]] = piece
                   render_board(board)
                else:
                    print("i'm sorry, that is an invalid move")

def new_game():
    global board
    render_board(board)
    game_terminal()

def inc(i, j):
    j += 1
    if(j == 8):
        i += 1
        j = 0
    return i, j

def load_game():
    FEN_filename = input("Please provide a path to a FEN string file\n> ")
    FEN_file = open(FEN_filename, "r")
    FEN_string = FEN_file.readline()
    i = 0
    j = 0
    global board
    for k in range(0, len(FEN_string)):
        if(FEN_string[k] in FEN_to_my_notation.keys()):
            board[i][j] = FEN_to_my_notation[FEN_string[k]]
            i, j = inc(i, j)
        elif(ord(FEN_string[k]) >= 0x30 and ord(FEN_string[k]) < 0x3a):
            for l in range(int(FEN_string[k])):
                board[i][j] = ""
                i, j = inc(i, j)    
        elif(FEN_string[k] == "/" or FEN_string[k] == "\n"):
            continue 
        else:
            print("Erroneous character in FEN string")
    render_board(board)
    game_terminal()

def start_game():
    action = input("Beginning game setup\nWould you like to \033[1;32mstart\033[0m a new game or \033[1;32mload\033[0m a board?\n> ")
    match(action):
        case "start":
            new_game()
        case "load":
            load_game()
        case "quit":
            print("Goodbye!")
            sys.exit(0)
        case _:
            print("I'm sorry, that is an unrecognized action. Please try again")
    

def parse_command(command):
    match(command):
        case "help":
            print("Available commands:")
            print(" - help: displays this message")
        case "quit":
            print("Goodbye!")
            sys.exit(0)
        case "play":
            start_game()
        case _ :
            print("Error - unsupported command!")
            sys.exit(1)


print_intro()
while True:
    command = input("> ")
    parse_command(command)