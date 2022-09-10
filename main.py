import PySimpleGUI as sg
from PIL import Image
from random import randint


# Creating player class
class Player:
    def __init__(self, games_won, symbol):
        self.games_won=games_won
        self.symbol=symbol


cross_player=Player(0, "cro.png")
nought_player=Player(0, "no.png")


#def active_player():

# Intially testing with active player symbol always X- can use this to test if player classes have worked

active_player_symbol = cross_player.symbol
active_player = cross_player





class Counter:
    def __init__(self, X_won, O_won, draws):
        self.X_won=cross_player.games_won
        self.O_won=nought_player.games_won


# Creating score counter function
#def score_counter():
    #if winner == cross_player:
        #cross_player.games_won+=1
   # elif winner == nought_player:
        #nought_player.games_won+=1
    #elif winner == draw:
        #draw_counter+=1

sg.theme('DarkRed1')   # Add a touch of color
image = "cro.png"

# Function to open second window after 'How to Play', showing who plays first. In first MVP, this defaults to X. Need to create randint function to alternate this later
def open_window1():
    layout = [[sg.Image(image, size=(200, 125))],
              [sg.Text('X plays first', size=(20,2), justification='center')],
              [sg.Button('Next', key="play")] ]
    window = sg.Window("Noughts & Crosses", layout, modal=True, element_justification='c')
    choice=None
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "play":
            window.close()
            initialise_game_board()

    window.close()


# Main environment for beginning 'How to Play' screen, leading to open_window function
def main():
    layout = [ [sg.Text('Noughts & Crosses', justification='center', font='bold')],
               [sg.Text('How to Play', size=(20, 1), justification='center')],
               [sg.Text('This is a TWO player game. Each player takes it in turn to place their X or O into one of the '
                     'empty squares in the grid by clicking on it. To win the game get three of your symbols in a '
                     'line horizontally, vertically or diagonally.', size=(40, 5))],
               [sg.Button('Play Game', key="play")] ]
    window = sg.Window('Noughts & Crosses', layout, element_justification='c')
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window
            break
        if event == "play":
            window.close()
            open_window1()


    window.close()


# Creating states for starting, playing, ending, and restarting (can call back on first player screen?)


#class State(starting):

MAX_ROWS = MAX_COL = 3

# Create gameplay here, with board and cells which will contain players' symbols once they play
def initialise_game_board():
    layout = [[sg.Button(' ', size=(8, 4),  key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
    layout += [[sg.Text('', size=(20,1), justification='center'), sg.Text('Scores', size=(20,1), justification='center')],
               [sg.Image('cro.png'), sg.Image('small_cro.png'), sg.Image('small_no.png')],
               [sg.Text('X to Play', size=(20,1), justification='center'), sg.Text('0    0', size=(20,1), justification='center')],
               [sg.Text('', size=(20,1), justification='center'), sg.Text('Draws: 0', size=(20,1), justification='center')]]
    turn = True
    window = sg.Window("Noughts & Crosses", layout, element_justification='c')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window
            break
        current_marker = window[event].get_text()
        window[event].update('X' if current_marker == ' ' and
                                    turn == True else 'O' if current_marker == ' ' and
                                    turn == False else 'X' if current_marker == 'X'
                                    else 'O' if current_marker == 'O' else ' ')
        if window[event].get_text() == 'X':
            turn = False
        elif window[event].get_text() == 'O':
            turn = True
        elif window['(1,1)'].update(turn=False):
            print("X wins!")
            break


    window.close()




if __name__ == "__main__":
    main()

