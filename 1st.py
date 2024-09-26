import random
#numbergame
print("let me think a number between 1 to 50")
s=random.randint(1,50)
d=input("Choose level of difficulty...Type 'easy' or 'hard'")
if d=="easy":
    y=10
    p=0
    print("you have 10 attemts to guess the number!")
    for i in range(0,10):
        
        r=int(input())
        if (r>s):
            print("ypur gess is Too High")
            print("Guess again")
        elif (r<s):
            print("your gess is Too Low")
            print("Guess again")
        else :
            print("congratulations the number is right!")
            p=1
            break
        if r!=s:
            print("you have ",(y-1),"attempts remaining to guess the number!")
            y=y-1
    if p==0:
        print("You are out of guesses... you lose!!")
else:
    y=5
    p=0
    print("you have 5 attemts to guess the number!")
    for i in range(0,5):
        
        r=int(input())
        if (r>s):
            print("ypur gess is Too High")
            print("Guess again")
        elif (r<s):
            print("your gess is Too Low")
            print("Guess again")
        else :
            print("congratulations the number is right!")
            p=1
            break
        if r!=s:
            print("you have ",(y-1),"attempts remaining to guess the number!")
            y=y-1
    if p==0:
        print("You are out of guesses... you lose!!")
    
    
        
    
