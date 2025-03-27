name = input("What's your name?")
print("Hello " + name + ", Let's play a looping game")

numbers = []

playing = "yes"
while playing == "yes":
    number = input("Give me a number from 1 to 10")
    number = int(number)
    numbers.append(number)
    if number <= 5:
        print("Yikes " + name + "." + str(number) + ", that's a small number. Let's triple it to " + str(number * 3) + "!")
    else:
        print("Wow " + name + "." + str(number) + ", that's a big number. Let's double it to " + str(number * 2) + "!")

    playing = input("Do you want to play again? (yes/no) : ")

print("You chose these numbers: " + str(numbers))
print("Thank you for playing! " + name + ", Hope we meet again soon.")
