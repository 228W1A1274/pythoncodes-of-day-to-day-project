import random
print("lets start the game")
w=0
e=0
while(1):
    d = random.choice(["rock", "paper", "scissors"])
    s=["rock","paper","scissors"]
    g=input("please select one from 'rock' 'paper' 'scissors': ")
    if g  not in s:
        print("please enter only between rock paper scissors: ")
        continue
    if d=="rock":
        if g=="rock":
            pass

        elif g=="paper":
            e=e+1
            print("you got one point ")
        else:
            w=w+1
            print("computer got one point ")

    elif d=="paper":
        if g=="rock":
            w=w+1
            print("computer got one point ")
        elif g=="paper":
            pass
        else:
            e=e+1
            print("you got one point ")
    else:
        if g=="rock":
            e=e+1
            print("you got one point ")
        elif g=="paper":
            w=w+1
            print("computer got one point ")
        else:
            pass
    a=input("enter 1 to continue: ")
    if a!="1":
        break
if w>e:
    print("computer has won the game ")
elif w==e:
    print("It is a tie ")
else:
    print("you won the game ")