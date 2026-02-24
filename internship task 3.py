# internship task 3 
# memory puzzel game with time limit of 60 seconds
import random
import time

# Create symbols (8 pairs = 16 cards)
symbols = ['A','B','C','D','E','F','G','H'] * 2
random.shuffle(symbols)

# Game board (hidden cards)
board = ['#'] * 16

def display_board():
    print("\nBoard:")
    for i in range(16):
        print(f"{board[i]} ", end="")
        if (i + 1) % 4 == 0:
            print()

def check_win():
    return '*' not in board

# Time limit (60 seconds)
time_limit = 60
start_time = time.time()

while True:
    display_board()
    
    # Check time
    if time.time() - start_time > time_limit:
        print("\n Time's up Game Over.")
        break
    
    try:
        first = int(input("Select first card (0-15): "))
        second = int(input("Select second card (0-15): "))
        
        if first == second or board[first] != '' or board[second] != '':
            print("Invalid selection! Try again.")
            continue
        
        # Reveal cards
        board[first] = symbols[first]
        board[second] = symbols[second]
        display_board()
        
        if symbols[first] != symbols[second]:
            print("Not a match!")
            time.sleep(1)
            board[first] = '#'
            board[second] = '#'
        else:
            print("Matched Keep going")
        
        if check_win():
            print("\n Congratulations! You won the game.")
            break
    
    except:
        print("Invalid input! Enter numbers between 0-15.")