number=100
while number<=999:
    a=number//100
    b=(number-a*100)//10
    c=number-a*100-b*10
    #print(a,b,c)
    if (a**3+b**3+c**3)==number:
        print(number)
    number+=1
