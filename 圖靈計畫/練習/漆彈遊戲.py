n,m = list(map(int,input().split()))
screen = []
for i in range(n):
    for i1 in range(n):
        screen.append(0)
ans = []





def trueli(l,x,y,n,screen,m):
    l1 = (l-1)/2
    if l1 <1:
        l1 = 0
    try :
        for i in range(n):
            screen[(y*i)*x] = m
            screen[(y*i)*x+l1] = m

        for i in range(n):
             screen[(x*i*5)*y] = m
             screen[(x*i*5)*y+l1] = m
    except :
        pass
    return screen





for i in range(1,m+1):
    l,x,y = list(map(int,input().split()))
    print(trueli(l,x,y,n,screen,i))
