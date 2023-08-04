import random
while True:
    # User input options:
    print('''1.Roll the dice  2.To exit ''')
    # Ask for user input.
    user = int(input("What would you like to do?"))
    # Print random integer from 1 - 20, the values of a standard D20 die.
    if user == 1:
        number = random.randint(1, 20)
        print(number)
    # If user chooses, option 2, the loop will break.
    else:
        break
