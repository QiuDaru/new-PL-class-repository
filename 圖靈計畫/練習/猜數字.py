import random 
x = random.randint(1,100)

while True:
    y =int(input("猜個數字 ? :"))

    if x == y :
        print("你答對了")
        break
    if y < x:
        print("太小")
    if y > x:
        print("太大")