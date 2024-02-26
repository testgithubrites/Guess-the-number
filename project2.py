import random
randNo = random.randint(1,100)
userguess=None
guesses=0
while(userguess!=randNo):
     userguess = int(input("\nEnter your guess"))
     guesses+=1
     if(userguess==randNo):
       print("\nYou guessed it right!!")
     else:
        if(userguess>randNo):
           print("\nyou guessed wrong , Enter small number")
        else:
           print("\nyou guessed wrong , Enter larger number")
print(f"\nYou guessed in {guesses} guesses")
with open("hiscore.txt","r") as f:
     hiscore=int(f.read())

     
if(guesses<hiscore):
     print("\nYou have just broken the high score!!")
     with open("hiscore.txt","w") as f:
        f.write(str(guesses))

