number=int(input("Please enter a number"))
s = 1
while number > 0:
    ji=s*number
    s=s+1
    if s == number:
        break
print(ji)
