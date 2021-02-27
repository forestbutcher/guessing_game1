attempts = []
number = ()
import random
x = random.randint(1,10)

print("Hello, this is a number guessing game. The point is to pick a random number between 1 and 10 in the fewest amount of guesses.  ")
print()
name = input("What is your name?  ")
print("Hello, {}!".format(name))

while True:
    number = input("Pick a number 1 through 10!  ")
    attempts.append(number)
    try:
        number = int(number)
    except ValueError:
        print("That is not a number!")
    else:
        try:
            if number > 10:
                raise ValueError("Your pick is over the number 10!")
        except ValueError as err:
            print("{}".format(err))
        if number < x:
            print("Too low!")
        if number > x:
            print("Too High!")
        if number == x:
            print()
            print("That is the correct number!")
            total_attempts = len(attempts)
            if total_attempts == 1:
                print("It took you {} attempt! Good guess!".format(total_attempts))
            else:
                print("It took you {} attempts!".format(total_attempts))
            print()
            play_again = input("Do you want to play again? Y/N  ")
            if play_again.lower() == "y":
                print()
                print("OK")
                print("It took you {} guesses last time.".format(total_attempts))
                attempts = []
                x = random.randint(1,10)
            else:
                print()
                print("Good Bye!")
                break
             





