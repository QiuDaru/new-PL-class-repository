inputs = int(input("輸入總和 :"))

g = 0 
for i in range(13): 
    g = g+1
    y = 0
    for i in range(13):
        y=y+1
        if g*4 +y ==inputs:
            print((str(g)+(" "))*4+str(y))
            exit()

   
