error=False
try:
    score=int(input("Please input your score as an integer:"))
except:
    print("Please enter a number")
    error=True
if error:
    print("Something wrong!")

else:    
    if score < 0 or score >100:
        print("Wrong score!")
    elif score < 60:
        print("Failed!!")
    elif score < 70:
        print("Passed!!!")
    elif score < 80:
        print("Medium!!!!")
    elif score < 90:
        print("Good!!!!!")
    elif score <= 100:
        print("Excellent!!!!!!")
