#Computer guesses the number you have in your mind
#You do not mention the number in your mind in the program itself
#It is only in your mind

import random

def computer_guess(start, end):
   
    guess = random.randint(start, end)
   
    while 1:
        ch = input(f"Is {guess} too high(H), too low(L) or correct(C)? -> ").upper()
        if ch not in ["H", "L", "C"]:
            print("Enter a valid response")
        else:
            break
    if ch == "H":
        computer_guess(start, guess-1)
    elif ch == "L":
        computer_guess(guess+1, end)
    elif ch == "C":
        print("Yay!! The computer got it correct!")
        return
   
max_num = int(input("Enter the maximum number of the range: "))

computer_guess(1, max_num)