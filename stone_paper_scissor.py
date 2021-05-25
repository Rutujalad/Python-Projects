import random
print("Welcome to the game.....")
x = 0
y = 0
for i in range (6):
    c = [1, 2, 3]
    b = random.choice(c)
    print("1.stone 2.scissor 3.paper")
    a = int(input())
    if a>3:
        print("You entered wrong number")

    else:
        if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1)  :
            print("you won")
            x += 1

        elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2) :
            print("you lost")
            y += 1

        else:
            print("it's tie...play agian")


print("Your score:",x)
print("Apponent score:",y)
if x>y:
    print("You won!!! Hurray...")
elif x == y :
    print("It's tie")
else:
    print("sorry...You lost")