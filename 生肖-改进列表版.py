birth_year = input("Please enter your birth year")

chinese_zodiac=["RAT","OX","TIGER","RABBIT",
                "DRAGON","SNAKE","HORSE","GOAT",
                "MONKEY","ROOSTER","DOG","PIG"]
try:
    birth_year = int(birth_year)
    guocheng = birth_year % 12
    if birth_year <1900:
        print("Are you kidding me?I think you were mummy.But I still tell you")
    if birth_year >2017:
        print("Are you from future?This is 2017.But I still tell you")
    print("Your Chinese Zodiac is ",chinese_zodiac[guocheng-4])
    if guocheng == 2:
        print('Me too')
except:
    print("Something wrong")
