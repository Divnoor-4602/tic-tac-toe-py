import numpy as np

inital_game_positions = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
symbols = {"cross": "X", "circle": "O"}
winning_combinations = []


space_line_count = 0
vertical_bar_count = 0


def spaces_per_game():
    print("---------")


def game_board_setup(game_array, initial_space_count, vertical_count):
    """sets up the np 2-D array every time the function is called"""
    for game_row in game_array:
        vertical_count = 0
        for game_column in game_row:
            vertical_count += 1
            print(game_column, end=" ")
            if vertical_count < 3:
                print("|", end="")
        print("\n")
        initial_space_count += 1
        if initial_space_count < 3:
            spaces_per_game()


def get_board_positions(user_choice_positions):
    position_chosen = user_choice_positions.split(" ")
    row_chosen = int(position_chosen[0]) - 1
    column_chosen = int(position_chosen[1]) - 1
    return row_chosen, column_chosen


def place_character(current_user_choice, player_num):
    row_current_user, column_current_user = get_board_positions(current_user_choice)
    if player_num == 1:
        inital_game_positions[row_current_user][column_current_user] = "X"
    elif player_num == 2:
        inital_game_positions[row_current_user][column_current_user] = "O"
    else:
        print("invalid player number")


def win_check(current_user_choice, current_positions):
    """Algorithm to check whose the winner"""
    row_current_user, col_current_user = get_board_positions(current_user_choice)
    # check if all elements in that row are the same
    if len(set(current_positions[row_current_user])) == 1:
        print("Winner")
    # extracting elements from a 2d column matrix and saving them in a list


game_board_setup(inital_game_positions, space_line_count, vertical_bar_count)

# Making user vs user
start = True
user = True

while start:
    if user == True:
        print("Player 1\n")
        position_place = input(
            "Player 1: Write the position to put the symbol on (eg., 2 3): "
        )
        place_character(position_place, 1)
        game_board_setup(inital_game_positions, space_line_count, vertical_bar_count)
        win_check(position_place, inital_game_positions)
        user = False
    elif user == False:
        print("Player 2\n")
        position_place = input(
            "Player 2: Write the position to put the symbol on (eg., 2 3): "
        )
        place_character(position_place, 2)
        game_board_setup(inital_game_positions, space_line_count, vertical_bar_count)
        user = True


# completed: Create a game board using np 2d arrays: Done
# inprog: Allow two game modes, 1: user vs user , 2nd: user vs computer
# inprog: Create an algorithm to check when a player wins, use consecutive columns and rows
# todo: Make a way to put user choice in the chose column
# todo: Should be a turn by turn system
