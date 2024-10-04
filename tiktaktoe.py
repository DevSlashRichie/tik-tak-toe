"""
This is a simple Tik Tak Toe game that will be used to demonstrate the use of
functions in Python. 
"""
from time import sleep
import random as rand
#import matplotlib.pyplot as plt

def create_board_box():
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

            cell_display = "\033[92m%s\033[0m" % cell_text if is_selected else cell
            print(cell_display, end=' | ')
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

def print_graphics_board(board):
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
            if board[i][j] == 'X':
                ax.text(j + 0.5, 2.5 - i, 'X', fontsize=40, ha='center', va='center')
            elif board[i][j] == 'O':
                ax.text(j + 0.5, 2.5 - i, 'O', fontsize=40, ha='center', va='center')

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
    import sys, termios, tty

    fd = sys.stdin.fileno()
    orig = termios.tcgetattr(fd)

    try:
        tty.setcbreak(fd)  # or tty.setraw(fd) if you prefer raw mode's behavior.
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, orig)

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
        A tuple that represents the updated position of the cursor.
    """
    while True:
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
        A tuple containing the updated history and board_box    

    """
    error = ""
    current_pos = (0, 0)
    while True:
        clean_screen()
        player1, player2 = players
        print_board(board, player1, player2, current_pos)

        last_player = history[-1] if len(history) > 0 else "X"
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
            history += next_player
            current_pos = (0, 0)
            error = ""

        next_pos = manage_input_in_board(input_text, current_pos)

        if next_pos:
            current_pos = next_pos

        #return history, board

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
        return f"Ok {player1_name} and {player2_name}, let's start the game\n{message}"

    print_loading(fn=fn)

    board = create_board_box()
    history = ""

    history, board = game_tick(history, board, (player1_name, player2_name))


if __name__ == "__main__":
    main()

