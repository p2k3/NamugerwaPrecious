countries = ["kenya", "uganda", "tanzania", "rwanda", "burundi"]

print("Welcome to the Country Guessing Game!")
print("I'm thinking of a country. Guess which one!")
print()

attempts = 0
correct = False

while attempts < 5:
    guess = input("Guess a country: ").lower()
    attempts += 1
    
    if guess == "":
        print("Please enter a valid country name")
        continue
    
    if guess in countries:
        print("Correct! You found the country: " + guess)
        correct = True
        break
    else:
        remaining = 5 - attempts
        if remaining > 0:
            print("Wrong guess. Try again. You have " + str(remaining) + " attempts left")
        else:
            print("Game Over! You used all your attempts")

if correct:
    print("You won the game in " + str(attempts) + " attempts!")
else:
    print("The country was: " + countries[0])
