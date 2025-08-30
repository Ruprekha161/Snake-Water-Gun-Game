
# Snake Water Gun Game

A simple Python command-line game based on the classic "Rock, Paper, Scissors" concept, but using Snake, Water, and Gun.

---

## Game Description

- This game lets you play against the computer.
- Choices:
  - **s** for Snake
  - **w** for Water
  - **g** for Gun
- Rules:
  - Snake drinks water (Snake wins against Water)
  - Water douses gun (Water wins against Gun)
  - Gun kills snake (Gun wins against Snake)

Each choice is internally represented by integers for game logic:
- 1 for Snake
- 0 for Gun
- -1 for Water

---

## How to Play

1. Run the Python script.
2. Input your choice when prompted (`s`, `w`, or `g`).
3. The computer randomly chooses its move.
4. Results are displayed stating who won or if it’s a draw.

---

## Code Example

```

import random

# Mapping user input to internal values

youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "snake", -1: "water", 0: "gun"}

yourstr = input("Enter your choice (s for snake, w for water, g for gun): ").strip().lower()

if yourstr not in youdict:
print("Invalid input! Please enter 's', 'w', or 'g'.")
exit()

you = youdict[yourstr]
computer = random.choice([0, -1, 1])

print(f"You chose {reversedict[you]}")
print(f"Computer chose {reversedict[computer]}")

if computer == you:
print("It's a draw!")
elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
print("You win!")
else:
print("You lose!")

```

---

## Requirements

- Python 3.x

---

## License

This project is open source and free to use.
