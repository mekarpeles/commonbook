"""Written on the fly for a demonstration. Feel free to optimize to your liking"""

import random

def proof():
    # door: 0 1 2 
    doors = ["goat", "goat", "car"]
    outcomes = []

    for i in range(1000):
        random.shuffle(doors)
        #Assuming we switch from door 1, let's see what happens 
        if doors[1] == "goat":
            outcomes.append("win" if doors[2] == "car" else "lose")
        if doors[2] == "goat":
            outcomes.append("win" if doors[1] == "car" else "lose")
    print(sum(1 for outcome in outcomes if outcome == "win") / 1000.0)

def play():
    outcomes = []
    welcome = "MONTY HALL WELCOMES YOU TO ... GOAT ... OR ... CAR!!!"
    print('=' * len(welcome))
    print(welcome)
    print('=' * len(welcome))
    while True:
        doors = ["Goat", "Goat", "Car"]
        random.shuffle(doors)

        print("\nGAME #%s:" % str(len(outcomes) + 1))
        print("+" + (("-"*5) + "+") * 3)
        print("|  %s  |  %s  |  %s  |" % tuple(range(3)))
        print("+" + (("-"*5) + "+") * 3)
        choice = input('Choose door 0, 1, or 2 (q to quit): ')

        if choice == "q":
            print("Goodbye! Thanks for playing!")
            break
        try:
            choice = int(choice)
            others = tuple({0, 1, 2}.difference({choice}))
            goat = others[0] if doors[others[0]] == "Goat" else others[1]

            print("\n")
            print("+" + (("-"*5) + "+") * 3)
            print("|  0  |  1  |  2  |".replace(str(choice), "*").replace(str(goat), "G"))
            print("+" + (("-"*5) + "+") * 3)

            while True:
                try:
                    c2 = int(input("(1) switch or (2) stay? "))
                    result = 1 if doors[c2] == "Car" else 0
                    outcomes.append(result)

                    print("\nYou %s!" % ("win" if result else "lose"))
                    print("+" + (("-"*5) + "+") * 3)
                    print("|  %s  |  %s  |  %s  |" % tuple([door[0] for door in doors]))
                    print("+" + (("-"*5) + "+") * 3)

                    print('-' * len(welcome))
                    print("You have won %s of %s games." \
                              % (sum(outcomes), len(outcomes)))
                    print('-' * len(welcome))
                    break
                except (ValueError, NameError):
                    print('Invalid selection.')
        except (ValueError, NameError):
            print('Invalid selection.')
                
if __name__ == "__main__":
    opt = input("(0) Play Game, (1) Run 'Always Switch' Proof: ")
    play() if opt else proof()
