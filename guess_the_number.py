import random
def is_valid_number(s):
    if s.isdigit() and 0 < int(s) <= 100:
        return True
    else:
        return False
def main():
    num = random.randint(1,100)
    guessed_num = False
    guess = str(input("Guess a number from 1 to 100: "))
    num_guesses = 0
    while not guessed_num:
        if not is_valid_number(guess):
            guess = str(input("I won't count that one. A number between 1 and 100:"))
        else:
            num_guesses += 1
            guess = int(guess)
        if guess < num:
            guess = str(input("Too low. Guess again:"))
        elif guess > num:
            guess = str(input("Too high. Guess again:"))
        else:
            print("You got it in ", num_guesses,  " guesses!")
            guessed_num = True
    print("Thanks for playing.")
if __name__ == '__main__':
    main()
