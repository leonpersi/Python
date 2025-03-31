import random

class Guesser:
    def __init__(self,name):
        self.name = name
        self.guesses = []

    def make_guess(self,guess,secret):
        self.guesses.append(guess)
        if guess < secret:
            print("Too low, " + self.name + ". Guess again")
            return False
        elif guess > secret:
            print("Too high, " + self.name + ". Guess again")
            return False
        else:
            print("Spot on! " + self.name + ". You did it!")
            return True


print("Welcome to Guess the Secret Number!")
name = input("What's your name?")
player = Guesser(name)

playing = "yes"
while playing == "yes":
    secret_number = random.randint(1, 100)
    print("I’ve picked a number between 1 and 100. Start guessing!")

    won = False
    while not won:
        guess = int(input("What is your guess? : "))
        won = player.make_guess(guess, secret_number)

    
    print("Nice job, " + player.name + "! It took you " + str(len(player.guesses)) + " guesses.")
    print("Your guesses were: " + str(player.guesses))


    player.guesses = []

    playing = input("Play again? (yes/no): ")

print("Thanks for playing, " + player.name + "!")
