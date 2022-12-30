#username generator
import random 
import time
first = ["Pineal", "Mythopoetic", "Feckless", "Unlearned", "Sweetish", "Iridian", "Sneakier" ]
last = ["Tooth", "Hotel", "Cabinet", "Oven", "Book", "List", "Moon", "Door"]
numbersone = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
numberstwo = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

user1 = random.choice(first)
user2 = random.choice(last)
numone = random.choice(numbersone)
numtwo = random.choice(numberstwo)
print("Your new Username is...")
time.sleep(1.5)
print(user1, user2, numone, numtwo, sep="")

