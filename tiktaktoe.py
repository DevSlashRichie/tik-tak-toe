"""
This is a simple Tik Tak Toe game that will be used to demonstrate the use of
functions in Python. 
"""
from time import sleep
import os

board_box = [[' ' for i in range(3)] for _ in range(3)]

def print_board(board, player1, player2):
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

    """
    print(f"P1: {player1} (X)")
    print(f"P2: {player2} (O)")
    print()

    for (i, row) in enumerate(board):
        for cell in row:
            print(cell, end=' | ')
        print()
        is_last_row = i == len(board) - 1

        if not is_last_row:
            print("-" * 12)

def clean_screen():
    """
    Clean the screen by printing a special character that clears the screen.
    """
    print("\033c", end="")

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

    if not name:
        print("Please enter a valid name")
        return None

    return name

def pruebas():
    """
    This function is used to test the game.
    """
    print_loading(seconds=2)
    print_board(board_box, "Player 1", "Player 2")
    name = ask_name()
    print(name)
    print_loading(1)
    clean_screen()
    print("Finished testing")

def check_testing():
    """
    Ask the user if they want to run the tests.

    Returns:
    --------
    bool
        True if the user wants to run the tests, False otherwise.
    """
    while True:
        is_var_set = "TEST" in os.environ
        is_test_from_env = os.environ.get("TEST") and bool(int(os.environ.get("TEST")))

        if is_var_set:
            if is_test_from_env:
                return True
            else:
                return False

        answer = input("Do you want to run the tests? (Y/n): ")
        is_test = answer.lower() == 'y' or answer.lower() == 'yes' or not answer

        if is_test:
            return True
        elif answer.lower() == 'n' or answer.lower() == 'no':
            return False
        else:
            print("Please enter a valid option")

def main():
    """
    The main function that will start the game.
    """
    print("Welcome to Tik Tak Toe")

    if check_testing():
        pruebas()
        exit(0)

    player1_name = ask_name("Player 1, tell me your name: ")
    player2_name = ask_name("Player 2, tell me your name: ")

    clean_screen()

    def fn(_counter, message):
        return f"Ok {player1_name} and {player2_name}, let's start the game\n{message}"

    print_loading(fn=fn)

    print_board(board_box, player1_name, player2_name)

if __name__ == '__main__':
    main()
