import random

def spin_reels():
    reel_symbols = ["cherry", "lemon", "orange", "plum", "watermelon"]
    return [random.choice(reel_symbols) for _ in range(3)]

def get_win_amount(reels):
    if reels[0] == reels[1] == reels[2]:
        return 100
    elif reels[0] == reels[1] or reels[1] == reels[2]:
        return 10
    else:
        return 0

def play_slot_machine():
    print("Welcome to the slot machine!")
    print("Spin the reels by pressing enter. Good luck!")
    while True:
        input("Press enter to spin the reels: ")
        reels = spin_reels()
        print(f"You spun {reels[0]}, {reels[1]}, {reels[2]}")
        win_amount = get_win_amount(reels)
        if win_amount > 0:
            print(f"Congratulations, you won ${win_amount}!")
        else:
            print("Sorry, you didn't win this time. Better luck next time!")

play_slot_machine()
