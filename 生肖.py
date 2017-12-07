birth_year = input("Please enter your birth year")

try:
    birth_year = int(birth_year)
except:
    print("Something wrong")

guocheng = birth_year % 12
if guocheng == 4:
    print("Your Chinese Zodiac is RAT")
elif guocheng == 5:
    print("Your Chinese Zodiac is OX")
elif guocheng == 6:
    print("Your Chinese Zodiac is TIGER")
elif guocheng == 7:
    print("Your Chinese Zodiac is RABBIT")
elif guocheng == 8:
    print("Your Chinese Zodiac is DRAGON")
elif guocheng == 9:
    print("Your Chinese Zodiac is SNAKE")
elif guocheng == 10:
    print("Your Chinese Zodiac is HORSE")
elif guocheng == 11:
    print("Your Chinese Zodiac is GOAT")
elif guocheng == 0:
    print("Your Chinese Zodiac is MONKEY")
elif guocheng == 1:
    print("Your Chinese Zodiac is ROOSTER")
elif guocheng == 2:
    print("Your Chinese Zodiac is DOG，me too")
elif guocheng == 3:
    print("Your Chinese Zodiac is PIG")
else:print("Unkown wrong")
