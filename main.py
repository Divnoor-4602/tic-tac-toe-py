import numpy as np

inital_game_positions = np.array(
    [[" ", "|", " ", "|", " "], [" ", "|", " ", "|", " "], [" ", "|", " ", "|", " "]]
)

space_line_count = 0


def spaces_per_game():
    print("---------")


def game_board_setup(game_array, initial_count):
    """sets up the np 2-D array every time the function is called"""
    for game_row in game_array:
        for game_column in game_row:
            print(game_column, end=" ")
        print("\n")
        initial_count += 1
        if initial_count < 3:
            spaces_per_game()


game_board_setup(inital_game_positions, space_line_count)

# Making user vs user


# todo: Create a game board using np 2d arrays: Done
# todo: Allow two game modes, 1: user vs user , 2nd: user vs computer
# todo: Make a way to put user choice in the chose column
# todo: Should be a turn by turn system
