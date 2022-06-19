print("Welcome to my Quiz Game!")

playing = input("Do You Want to play? ")

if playing != "yes":
    quit()

print("Okay let's play :)")

answer = input("What does CPU stand for? ")

if answer == "central processing unit":
    print("Correct!")