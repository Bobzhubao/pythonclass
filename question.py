score = 0

birth = input("My birthday , input by MM.DD")
birth_a ="06.26"
if birth == birth_a:
    score = score + 1
    print("got 1 point.new score=",score)
game = input("My favourite game")
game_a ="ninja"
if game == game_a:
    score = score + 1
    print("got 1 point.new score=",score)
colour = input("My favourite colour")
colour_a ="blue"
if colour == colour_a:
    score = score + 1
    print("got 1 point.new score=",score)
fruit = input("My favourite fruit")
fruit_a ="pineapple"
if fruit == fruit_a:
    score = score + 1
    print("got 1 point.new score=",score)
computer =input("My laptop model")
computer_a="MacBook Air"
if computer == computer_a:
    score = score + 1
    print("got 1 point.new score=",score)

if score == 5:
    print("Excellent")
elif score == 4:
    print("Good")
elif score == 3:
    print("Not too bad")
elif score == 2:
    print("Bad")
elif score == 1:
    print("Very bad")
elif score == 0:
    print("Ah!!!!!!")
