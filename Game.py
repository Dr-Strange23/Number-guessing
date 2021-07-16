import random 

print ("guessing game")

number = random.randint(1,9)

chances = 0

# While loop to count the number of chances 
while chances < 5:
    guess = int(input("enter your guess- "))

    if guess == number:
    # if number entered by user is same as the generated 
    # number by randit function then break from loop using loop
    # control statement "break"
        print("Congratulation you win!!!")
        break
    elif guess<number:
        print ("your guess was too low, guess a number higher than ", guess)
    else:
        print ("your guess was too high, guess a number lower than", guess)

    chances+=1

# Check whether the user gessed the correct number 
    if not chances < 5:
        print("YOU LOSE!!! The number is", number)


# Compare the user entered number with the number to be guessed


































