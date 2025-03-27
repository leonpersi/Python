name = input("What's your name?")
print("Hello " + name + ", Let's play a game")

number = input("Give me a number from 1 to 10")

number = int(number)

if number <= 5:
    print("Yikes " + name + "." + str(number) + ", that's a small number. Let's triple it to " + str(number * 3) + "!")
else:
    print("Wow " + name + "." + str(number) + ", that's a big number. Let's double it to " + str(number * 2) + "!")
