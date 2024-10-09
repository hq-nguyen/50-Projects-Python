import random
from rich.console import Console
from rich.text import Text

# Initialize the rich console for colorful output
console = Console()

# Define the dice faces using ASCII art
dice_faces = {
    1: (
        "---------\n"
        "|       |\n"
        "|   O   |\n"
        "|       |\n"
        "---------"
    ),
    2: (
        "---------\n"
        "| O     |\n"
        "|       |\n"
        "|     O |\n"
        "---------"
    ),
    3: (
        "---------\n"
        "| O     |\n"
        "|   O   |\n"
        "|     O |\n"
        "---------"
    ),
    4: (
        "---------\n"
        "| O   O |\n"
        "|       |\n"
        "| O   O |\n"
        "---------"
    ),
    5: (
        "---------\n"
        "| O   O |\n"
        "|   O   |\n"
        "| O   O |\n"
        "---------"
    ),
    6: (
        "---------\n"
        "| O   O |\n"
        "| O   O |\n"
        "| O   O |\n"
        "---------"
    )
}

# Function to simulate dice roll
def roll_dice():
    result = random.randint(1, 6)
    console.print(Text(f"\nYou rolled a {result}!", style="bold green"))
    console.print(dice_faces[result])

# ask user how many times they want to roll the dice
def roll_dice_n_times():
    time = int(input("How many times do you want to roll the dice? "))
    total = 0
    for i in range(time):
        result = random.randint(1, 6)
        console.print(dice_faces[result])
        total += result
    console.print(Text(f"\n Your score is {total} !", style="bold green"))

# Main program loop
while True:
    user_input = input("\nRoll the dice? (y/n): ").strip().lower()
    if user_input in ['y', 'yes']:
        roll_dice_n_times()
    elif user_input in ['n', 'no']:
        console.print(Text("\nGoodbye!", style="bold blue"))
        break
    else:
        console.print(Text("Invalid input, please enter 'y' or 'n'.", style="bold red"))
