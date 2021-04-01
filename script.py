from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks:

#Empty list to store stacks
stacks = []

#Creating three Stack instances
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

#Adding each Stack instances to the lsit
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)


#Set up the Game:

#Asking user to input numner of disks for the game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

#Checking to ensure that there is at leadt 3 disks for the game. 
while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

#Creating for loop to add disks to left stack
for disk in range(num_disks, 0, -1):
    left_stack.push(disk)

#Deisplaying to the user the optimal moves in their game setup
num_optimal_moves = 2 ** (num_disks - 1)
print("\nThe fastest you can solve this game is in {} moves".format(num_optimal_moves))

#Get User Input:

#Helper function to prompt user to choose a stack
def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {letter} for {name}".format(letter=letter, name=name))

        user_input = input("")

        if user_input in choices:
            for i in range(len(stacks)):
                if user_input in choices[i]:
                    return stacks[i]
            
#Play the Game:

num_user_moves = 0

while(right_stack.get_size() != num_disks):
    print("\n\n\n...Current Stacks...")
    for stack in stacks:
        stack.print_items()
    
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again")

print("\n\nYou completed the game in {user_moves} moves, and the optimal number of moves is {optimal_moves}".format(user_moves = num_user_moves, optimal_moves = num_optimal_moves))

