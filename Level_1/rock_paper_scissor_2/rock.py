# library
import random
from rich.console import Console
from rich.text import Text
console = Console()
# create win pair
win_pair =[('rock', 'lizard'),
           ('scissors', 'paper'),
           ('paper', 'rock'),
           ('lizard', 'spock'),
           ('spock', 'scissors'),
           ('scissors', 'lizard'),
           ('lizard', 'paper'),
           ('paper', 'spock'),
           ('spock', 'rock'),
           ('rock', 'scissors')]

# create choice
choice = ['rock', 'paper', 'scissors', 'lizard', 'spock']
# create random choice for computer
computer = random.choice(choice)

# create user choice with while loop
print("\n\nLet's play game!")
# funtion to check user input
def play_game():
    while True:
        try:
            print('Choose: rock, paper, scissors, lizard, spock as:\n 0-->rock\n 1-->paper\n 2-->scissors\n 3-->lizard\n 4-->spock')
            user_choice = int(input('Enter your choice: ')) 
            if user_choice in range(0, 5):
                print('-------------------------------------')
                console.print(Text(f"\nYou choose: {choice[user_choice]}", style="bold yellow"))
                console.print(Text(f"Computer choice: {computer}", style="bold blue"))
                if choice[user_choice] == computer:
                    print('Draw')
                elif(choice[user_choice], computer) in win_pair:
                    print('You win')
                else:
                    print('You lose')
                print('-------------------------------------')
                break
            else:
                console.print(Text(f"\nPlease enter number (0-4)", style="bold red"))
                continue
        except ValueError:
            console.print(Text(f"\nPlease enter number (0-4)", style="bold red"))
            continue
play_game()
# check user continue playing or not
while True:
    try:
        play_again = input('Do you want to play again?').strip().lower()
        if play_again in ['y', 'yes']:
            play_game()
        elif play_again in ['n', 'no']:
            console.print(Text(f"\nThank you for playing", style="bold green"))
            break
        else:
            console.print(Text(f"\nPlease enter y/n", style="bold red"))
    except Exception as e:
        print(e)
    
