# Sarah Steinbaum

# Define the instructions and commands
def show_instructions():
    # print a main menu and the commands
    print("The Vampire's Mansion Text Adventure Game")
    print("Collect all 6 items to win the game, or be eaten by the Vampire.")
    print("Move Commands: South, North, East, and West")
    print("Add to Inventory: Get 'item name'")


# Define the main function of the game
def main():
    show_instructions()
    # A dictionary linking a room to other rooms
    # and linking one item for each room except the Start room (Foyer) and the room containing the villain
    rooms = {
        'Foyer': {'East': 'Den', 'item': 'None'},  # Start room
        'Den': {'North': 'Kitchen', 'West': 'Foyer', 'East': 'Shed', 'South': 'Bedroom', 'item': 'matches'},
        'Kitchen': {'South': 'Den', 'East': 'Dining Room', 'item': 'garlic'},
        'Dining Room': {'West': 'Kitchen', 'item': 'knife'},
        'Bedroom': {'North': 'Den', 'East': 'Bathroom', 'item': 'wooden-stake'},
        'Bathroom': {'West': 'Bedroom', 'item': 'holy-water'},
        'Shed': {'West': 'Den', 'North': 'Cellar', 'item': 'kerosene'},
        'Cellar': {'South': 'Shed', 'item': 'vampire'}  # Villain
    }
    # Inventory is set to empty
    inventory = []
    # The user is currently in the Foyer
    current_room = 'Foyer'

    # Use a while loop to create a gameplay loop that will iterate based on the user's input
    while True:
        # The variable, moves, will be assigned to the current room from the dictionary, rooms
        moves = rooms[current_room]
        # Shows the user's status on what room they are in
        print('\nYou are in the', current_room)
        # Provide the user with options they can choose to input
        print('Your moving options are: ')
        # Use if statements within the while loop for decision branching
        # This will move user in a direction according to their input or allow them to obtain an item
        if 'North' in moves:
            # Output the direction option to the user and the room that direction will take them to
            print(' - North:', moves['North'])
        if 'East' in moves:
            print(' - East:', moves['East'])
        if 'South' in moves:
            print(' - South:', moves['South'])
        if 'West' in moves:
            print(' - West:', moves['West'])
        # If there is an item in the room, the output will show which item is in the current room
        if rooms[current_room]['item'] != 'None':
            print('You see', rooms[current_room]['item'])
            # Displays current items in inventory
            print('Inventory: ', ', '.join(inventory))
        print('---------------------------------')
        # Prompt the user to input a direction
        next_move = input('Enter your move: ')
        next_move = next_move.capitalize()

        # If the next move is valid, the user will move according to the user's input
        if next_move in moves.keys():
            current_room = moves[next_move]
        # If 'Get' is in the input the item following 'Get' will be added to the inventory
        elif 'Get' in next_move:
            next_move = next_move.split()
            # Allows input to be lower cased
            next_move = next_move[1].lower()
            # If the item is invalid, 'invalid item' will appear and prompt the user for new input
            if next_move != rooms[current_room]['item']:
                print('Invalid item')
            # If the input is valid, it will be added to the inventory
            else:
                rooms[current_room]['item'] = 'None'
                inventory.append(next_move)
        # If the input is not valid 'Input Validation' will appear and prompt the user for new input
        else:
            print('Input Validation')
        # When the user enters the Cellar, they will either win or lose depending on the amount of items they have
        if current_room == 'Cellar':
            # If the user found all 6 items, the game will congratulate them then end
            if len(inventory) == 6:
                print('Yay! You got all the items needed to kill the vampire! You win!')
               # break
            # If the user did not get all 6 items, they lose and the game will end
            elif len(inventory) < 6:
                print('Oh no! You do not have enough items to kill the vampire! Looks like you are his supper...')
                #break


# End main
main()
