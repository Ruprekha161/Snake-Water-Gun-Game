import random

'''
1 for snake
0 for gun
-1 for water
'''

youdict = {"s":1, "w":-1, "g":0}
reversedict = {1:"snake", -1:"water", 0:"gun"}

yourstr = input("Enter your choice (s for snake, w for water, g for gun): ").strip().lower()
if yourstr not in youdict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
    exit()

you = youdict[yourstr]
computer = random.choice([0, -1, 1])

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

# Game logic
if computer == you:
    print("It's a draw!")
elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
    print("You win!")
else:
    print("You lose!")