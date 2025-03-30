class Player:
    def __init__(self, name):
        self.name = name
        self.numbers = []
        self.rounds = 0
        pass

    def check_number(self,number):
        self.numbers.append(number)
        if number <=4:
            print("Yikes, " + self.name + ". That's a small number. It's now:" + str(number*3) + "!" )
        elif number >=5 and number <=10:
            print("Wow, " + self.name + ". That's a big number. It's now:" + str(number*2) + "!" )
        else:
            print("Oof, " + self.name + ". That's a too big number. It's now:" + str(number*0) + "!" )

name = input("What's your name? ")
player = Player(name)
print("Hey " + player.name + ", Let's play a game!")
playing = "yes"
while playing == "yes":
    player.rounds = player.rounds+1
    number = int(input("Please choose a number between 1 - 10 "))
    player.check_number(number)
    playing = input("Do you want to play again? (yes/no) ")
print("Thanks for playing, " + player.name + "! You picked: " + str(player.numbers) + ". You played for: " + str(player.rounds) + "!")