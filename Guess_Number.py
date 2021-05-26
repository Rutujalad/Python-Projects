
a=57
ca=9
for i in range (9):
    print("Guess the no.:")
    b=int(input())
    if a > b:
        print("No. is less than actual no.")
        ca=ca-1
    elif b > a:
        print("No.is bigger than actual no.")
        ca=ca-1
    else:
        print("you guessed it correct")
        break
    print("You left ",8-i,"this much guess")

if ca==0:
    print("sorry...You lost")
    
