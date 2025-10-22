import random 
n = random.randint(1,100)
a=-1
guesses = 1
while(a != n):
    a= int(input("Guess the  number! from 1 to 100 : "))
    if(a>n):
        print("Enter lower no. please")
        guesses +=1
    elif(a<n):
        print("Enter higher no. please")
        guesses +=1  

print(f"You have guessed the correct no. {n} in {guesses} attempts")      
