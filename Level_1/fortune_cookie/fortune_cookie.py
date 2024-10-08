import random

fortunes =[
    "Good news will come to you from far away.",
    "You will achieve your greatest ambitions through perseverance.",
    "A thrilling time is in your near future.",
    "Happiness is not in the destination, but in the journey.",
    "Someone close to you has a valuable piece of advice for you.",
    "Opportunities are like sunrises—if you wait too long, you miss them.",
    "An unexpected event will bring you great joy."
]

# make a cookie
yes = ["yes","y"]
no = ["no", 'n']

# check user option

while True:
    try:
        print("\n\n=================================================================================")
        cookie = input("You are given a fortune cookie today! Do you want to open this one? (y/n): ").strip().lower()
        
        if cookie in yes:
            print("\n" + random.choice(fortunes))
            break  
        elif cookie in no:
            print("\nThank you!")
            break  
        else:
            print("\nInvalid input. Please type 'y' for yes or 'n' for no.\n")
    except Exception as e:
        print(e)

print("\n=================================================================================")

