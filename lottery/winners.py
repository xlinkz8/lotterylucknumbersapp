


# import random
# winners_number = random.sample(range(51),10)
# print(" The winner's numbers is:", winners_number)
# num =int(input("Enter a number: "))
# if num == 30:
#     print("Congratulation, you are the lucky winner!.")
# elif num in winners_number:
#     print("You got the lucky number, but not the winning number")
# else:
#     print("Hey buddy! try again later.")

#pseudocode
# user enters his name
# generate a set of winners numbers
# user input number generated
# check if user matches winners numbers
# if it matches the winners number
#     print congratulaitions you won
# if not print you got the lucky number not the winners number

import random
user = input("Enter your Name: ")
lottery_numbers = set(random.sample(range(51),50))
print(" The winner's numbers is:", lottery_numbers)
num = int(input("Enter a number from 0 and 50: "))
if lottery_numbers == num :
    print("Congratulation",user,"you are the lucky winner!.")
# elif num in winners_number:
#     print(user, "You got the lucky number, but not the winning number")
else:
    print( user ,"Try again later.")
