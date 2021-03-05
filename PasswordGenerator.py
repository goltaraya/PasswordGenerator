# Password Generator Project ------> Author: Yago Goltara
import random
import time

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Greetings
print("Welcome to the Password Generator!")

# Get the size of each list(let,sym,num)
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Create a variable to save the password
password = ""

# Choose random letters and save in "password"
for n in range(0,nr_letters):
    x = random.choice(letters)      # .choice() is used when you randomly want to pick up an item
    password += x                   # from a List/Sequence

# Choose random symbols and save in "password"
for n in range(0,nr_symbols):
    x = random.choice(symbols)
    password += x

# Choose random numbers and save in "password"
for n in range(0,nr_numbers):
    x = random.choice(numbers)
    password += x

# Turn str() into list()
list_password = list(password)

# Shuffle the list created
random.shuffle(list_password)

# Interate with the user
print("Wait a second... Your password's being created.")
time.sleep(1.5)             # Freeze the screen for 1.5 sec 

# Turn the list() into str() back again
final_password = ''.join(list_password)

# Print out the password generated 
print(f"The password generated is: {final_password}")
input()                 # Conditing to stop the program without kill it