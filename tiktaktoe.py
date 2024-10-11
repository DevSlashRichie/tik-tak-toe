"""
This is a simple Tik Tak Toe game that will be used to demonstrate the use of
functions in Python. 
"""
from time import sleep
import random as rand
import matplotlib.pyplot as plt
from datetime import datetime
import os
import sys

import matplotlib


if os.name == "nt":
    import msvcrt

    # if we are on windows we use the Qt5Agg backend
    matplotlib.use("WebAgg")
else:
    import termios, tty

def create_board_box():
    """
    Create a 3x3 board with empty cells.

    Returns:
    --------
    list
        A 2D list that represents the board
    """
    return [[' ' for i in range(3)] for _ in range(3)]

def print_board(board, player1, player2, seleted_index):
    """
    Print the board with the players' names. This acts as the game arena.

    Parameters:
    -----------
    board: list
        A 2D list that represents the board
    player1: str
        The name of player 1
    player2: str
        The name of player 2
    selected_index: tuple
        The index of the selected cell

    """
    print(f"P1: {player1} (X)")
    print(f"P2: {player2} (O)")
    print()

    for (i, row) in enumerate(board):
        for j, cell in enumerate(row):
            is_selected = (i, j) == seleted_index

            cell_text =  "*" if cell == " " else cell

            cell_display = "\033[92m%s\033[0m" % cell_text if is_selected \
            else cell
            print(cell_display, end=' | ')
        print()
        is_last_row = i == len(board) - 1

        if not is_last_row:
            print("-" * 12)


def clean_screen():
    """
    Clean the screen by printing a special character that clears the screen.
    """
    #print("\033c", end="")

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def print_loading(seconds = 4, fn = None):
    """
    Print a loading message for a given amount of seconds.

    Parameters:
    -----------
    seconds: int
        The amount of seconds to print the loading message.
    fn: function
        A function that receives the current counter and the loading message. 
        It should return a string that will be printed on the screen.
    """
    counter = 0
    while counter < seconds:
        amount_of_dots = counter % 4
        loading_message = "Loading" + "." * amount_of_dots
        if fn:
            print(fn(counter, loading_message))
        else:
            print(loading_message)
        sleep(1)
        counter += 1
        clean_screen()

def ask_name(message = "Tell me your name: "):
    """
    Ask the user for their name. This function won't return until the user
    enters a valid name.

    Parameters:
    -----------
    message: str
        The message to display when asking for the name.
    
    Returns:
    --------
    str
        The name of the player
    """
    name = ""
    while not name:
        name = input(message)

    return name


def print_graphics_board(board):
    """
    Print the board using a graphical representation.
    """
    fig, ax = plt.subplots()

    # Set the limits and remove ticks
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_xticks([])
    ax.set_yticks([])

    # Draw the grid
    for i in range(1, 3):
        ax.axhline(i, color='black', lw=2)
        ax.axvline(i, color='black', lw=2)

    # Plot the Xs and Os
    for i in range(3):
        for j in range(3):
            cell_text = board[i][j]
            if cell_text != " ":
                ax.text(j + 0.5, 2.5 - i, cell_text, fontsize=40, ha='center', \
                        va='center')

    # Show the plot
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def print_menu():
    """
    Print the menu of the game.
    """
    print("1. Start game")
    print("2. Run tests")
    print("3. Exit")

def request_menu():
    """
    Request the user to select an option from the menu.

    Returns:
    --------
    int
        The option selected by the user.
    """
    while True:
        print_menu()
        option = input("Select an option: ")

        if option == "1":
            return 1
        elif option == "2":
            return 2
        elif option == "3":
            print("bye!")
            exit(0)
            return None
        else:
            print("Please select a valid option")

def print_end_menu():
    """
    Print the end menu of the game.
    """
    print("1. Play again")
    print("2. Print History")
    print("3. Print Board")
    print("4. Exit")

def request_end_menu():
    """
    Request the user to select an option from the end menu.

    Returns:
    --------
    int
        The option selected by the user.
    """
    while True:
        print_end_menu()
        option = input("Select an option: ")

        if option == "1":
            return 1
        elif option == "2":
            return 2
        elif option == "3":
            return 3
        elif option == "4":
            print("bye!")
            exit(0)
            return None
        else:
            print("Please select a valid option")

def print_banner(text):
    """
    Print a banner with the given text.

    Parameters:
    -----------
    text: str
        The text to display in the banner.
    """
    print("=" * 40)
    print()
    print(text)
    print()
    print("=" * 40)



def getch():
    """
    Get a single character input from the user.
    """

    if os.name == "nt": # for windows
        return msvcrt.getch().decode('utf-8')

    # for linux
    fd = sys.stdin.fileno()
    orig = termios.tcgetattr(fd)

    try:
        tty.setcbreak(fd)  
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, orig)

def check_game_over(board):
    """
    Check if the game is over.

    Parameters:
    -----------
    board: list
        A 2D list that represents the board

    Returns:
    --------
    bool
        True if the game is over, False otherwise.
    """
    
    # iter the whole matrix
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    
    return True


def check_winner(board):
    """
    Check if there is a winner in the game.

    Parameters:
    -----------
    board: list
        A 2D list that represents the board

    Returns:
    --------
    str
        The name of the winner or 'XO' if it's a tie, or None if there is no winner yet.
    """
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] \
            and board[0][col] != " ":
            return board[0][col]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ": 
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    if check_game_over(board):
        return "XO"

    return None


def manage_input_in_board(input_text, current_pos):
    """
    This function will manage the input in the board.

    Parameters:
    -----------
    input_text: str
        The input text from the user.
    current_pos: tuple
        A tuple that represents the current position of the cursor.

    Returns:
    --------
    tuple
        A tuple containing the new position of the cursor.
    """
    if input_text == "w":
        return (max(0, current_pos[0] - 1), current_pos[1])
    elif input_text == "s":
        return (min(2, current_pos[0] + 1), current_pos[1])
    elif input_text == "a":
        return (current_pos[0], max(0, current_pos[1] - 1))
    elif input_text == "d":
        return (current_pos[0], min(2, current_pos[1] + 1))
    else:
        return None

def game_tick(history, board, players):
    """
    This function will handle the game tick.

    Parameters:
    -----------
    history: string
        A list of the moves made by the players
    board: list
        A 2D list that represents the board

    Returns:
    --------
    tuple
        A tuple containing the updated history and board_box and the winner.
    """
    error = ""
    current_pos = (0, 0)
    while True:

        clean_screen()
        player1, player2 = players
        print_board(board, player1, player2, current_pos)

        # we check the winner here in order to draw the latest board
        possible_winner = check_winner(board)
        if possible_winner:
            return history, board, possible_winner

        last_player = history[-1][0] if len(history) > 0 else "X"
        next_player = "X" if last_player == "O" else "O"

        banner = "Player %s's turn" % next_player

        if error:
            banner += f"\n\033[91m{error.upper()}\033[0m"

        print_banner(banner)

        input_text = getch()

        if input_text == "p":
            if board[current_pos[0]][current_pos[1]] != " ":
                error = "This cell is already taken"
                continue

            board[current_pos[0]][current_pos[1]] = next_player
            history.append((next_player, current_pos[0], current_pos[1]))
            current_pos = (0, 0)
            error = ""

        next_pos = manage_input_in_board(input_text, current_pos)

        if next_pos:
            current_pos = next_pos

def save_history_into_file(history, player1, player2, winner):
    """
    Save the history into a file.

    Parameters:
    -----------
    history: list
        A list of the moves made by the players
    """

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # we append to the end of the file
    with open("history.txt", "a") as f:
        line = "Date: %s\nPlayer O: %s vs. Player X: %s\nWinner:%s\nHistory %s\n\n" \
            % (date, player1, player2, winner, history)

        f.write(line)



def pruebas():
    """
    This function is used to test the game.
    """
    print_loading(seconds=2)
    name = ask_name()
    print(name)
    print_loading(1)
    clean_screen()

    print("Testing the game")
    print("Creating the board")
    board = create_board_box()
    assert board == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    print_board(board, "Player 1", "Player 2", (0, 0))
    print_banner("Board created successfully")

    print("Checking the game over")
    assert not check_game_over(board)
    print_banner("Game over checked successfully")

    print("Checking the winner")
    assert not check_winner(board)
    print_banner("Winner checked successfully")

    print("Checking the input in the board")
    new_pos = manage_input_in_board("w", (0, 0))
    assert new_pos == (0, 0)

    new_pos = manage_input_in_board("s", (0, 0))
    assert new_pos == (1, 0)

    new_pos = manage_input_in_board("a", (0, 0))
    assert new_pos == (0, 0)

    new_pos = manage_input_in_board("d", (0, 0))
    assert new_pos == (0, 1)

    print_banner("Input in the board checked successfully")

    print("Checking the game tick")
    history, board, winner = game_tick([], board, ("Player 1", "Player 2"))
    assert winner

    print_banner("Game tick checked successfully")

    clean_screen()

    print_banner("Finished testing")

def main():
    """
    The main function that will start the game.
    """
    print("Welcome to Tik Tak Toe")

    print()

    # instructions

    print("Instructions:")
    print("1. Use the keys 'w', 'a', 's', 'd' to move the cursor")
    print("2. Press 'p' to place the mark")
    print()


    option = request_menu()

    if option == 2:
        pruebas()
        return  

    player1_name = ask_name("Player 1, tell me your name: ")
    player2_name = ask_name("Player 2, tell me your name: ")

    clean_screen()

    def fn(_counter, message):
        msg = f"Ok {player1_name} and {player2_name}, let's start the \
game\n{message}"
        # we do an easteregg here
        if player1_name == player2_name:
            msg += "\n\nYou both have the same name, that's cool!"
        return msg

    print_loading(fn=fn)

    board = create_board_box()
    
    # history should have entries of the form (player, row, col)
    history = []

    history, board, winner = game_tick(history, board, (player1_name, \
                                                        player2_name))

    print()
    if winner:
        if winner == "XO":
            print("It's a tie!")
        else:
            print(f"Player {winner} wins!")

    print()

    save_history_into_file(history, player1_name, player2_name, winner)

    def run_end():
        end_option = request_end_menu()

        if end_option == 1:
            main()
        elif end_option == 2:
            print(history)
            run_end()
        elif end_option == 3:
            print_graphics_board(board)
            run_end()
        else:
            print("bye!")
            exit(0)

    run_end()



if __name__ == "__main__":
    main()

