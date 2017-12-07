score=int(input("Please input your score"))

if score >= 101 or score < 0:
    print("Wrong score!")
elif score >= 90:
    print("Excellent!!!!!!")
elif score >= 80:
    print("Good!!!!!")
elif score >= 70:
    print("Medium!!!!")
elif score >= 60:
    print("Passed!!!")
elif score >= 0:
    print("Failed!!")

