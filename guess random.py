import random  
secret=random.randint(1,100) 
#print (secret)  
time=6 
guess=0
minnumber=0 
maxnumber=100 
print("Welcome to the guess place，please start")  
while guess!=secret and time>=0: 
    guess=int(input("*The number is between 0-100，plase enter your number:"))  
    print("Your guess number is：",guess)  
    if guess==secret:  
        print("You're right，good!")  
    else:  
        #当不等于的时候，还需要打印出相应的区间，让用户更容易使用  
        if guess<secret:  
            minnumber=guess  
            print("Your guess number smaller than my number")              
            print("Now the number is between：",minnumber,"-",maxnumber)  
        else:  
            maxnumber=guess  
            print("Your number bigger than my number")  
            print("Now the number is between：",minnumber,"-",maxnumber)  
        print("It's regretted，You're wrong，You still have",time,"chance")  
    time-=1  
print("Game over")  
