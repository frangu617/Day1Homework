# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
def hello():
    print("hello")

hello()

# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements
def pack(a, b, c):
    return [a, b, c]


# A function called pack_input() that takes input from the user and uses the pack() function to return a list of that input
def pack_input():
    user_input_one = input("Enter first item: ")
    user_input_two = input("Enter second item: ")
    user_input_three = input("Enter third item: ")
    print (pack(user_input_one, user_input_two, user_input_three))

#running pack_input()
pack_input()

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything
def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty!")
    else:
        for item in lunch_list:
            if lunch_list.index(item) == 0: 
                print(f"First I eat the {item}")
            else:
                print(f"Next I eat the {item}")

def lunch_input():
    lunch_list = []
    done = False
    while not done:
        user_input = input("Enter an item: ")
        lunch_list.append(user_input)
        more_stuff = input("more? (y/n) ")
        if more_stuff.lower() == "n":
            done = True
    return lunch_list

# Get lunch items from user
lunch_items = lunch_input()

# Eat lunch
eat_lunch(lunch_items)
eat_lunch([])
