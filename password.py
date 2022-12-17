#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Ultimate password Generator! lol")
allLetters= int(input("How many letters would you like in your password?\n")) 
allSymbols = int(input(f"How many symbols would you like?\n"))
allNumbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, allLetters + 1):
    ltr=random.choice(letters)
    # Randomly decide uppercase or lowercase version of the letter
    password_list.append(ltr if (random.randint(2,100)%2==0) else ltr.upper())

#Adding symbols to our list of letters
for char in range(1, allNumbers + 1):
  password_list += random.choice(numbers)

#Adding symbols to our list of letters
for char in range(1, allSymbols + 1):
  password_list += random.choice(symbols)



# Now Le't do a bit of shaffling
random.shuffle(password_list)

#Our holly password
password = ""
for char in password_list:
  password += char
print(f"\nYour holly password is: {password}")
