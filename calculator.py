error:False

try:
    first=input("Please enter a number")
except:
    print("Please input a number")
error=True

try:
   second=input("Please enter a number")
except:
    print("Please input a number")
error=True

symbol=input("Please enter a symbol")
first=int(first)
second=int(second)
if symbol== "/" and second ==0:
    print("Something wrong!")

if error:
    print("Something wrong!")

if symbol == "+" :
    print("The answer is ",first + second)
elif symbol == "-" :
    print("The answer is ",first - second)
elif symbol == "*" :
    print("The answer is ",first * second)
elif symbol == "/" :
    print("The answer is ",first / second)
elif symbol == "**" :
    print("The answer is ",first ** second)
else:print("Please input number and symbol.Please try again")
