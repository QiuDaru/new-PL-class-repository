ton = input()
ton = list(ton)

ans = []
a = 0
b = 0
if "a" in ton:
    a = int(ton.index("a"))
    a = a+1
if "b" in ton:
    b = int(ton.index("b"))
    b = b+1

try:
    for a1 in range(a,b):
        for b1 in range(b,int(len(ton))+1):
            for c in range(b,int(len(ton))+1):
                
                if 1<= int(a1) and int(a1)<int(b1) and int(b1)<int(c) and int(c)<=int(len(ton)):
                        
                    ans.append((a1+1,b1+1,c+1))

except:
    pass

if len(ans)%2 == 0:
    print("DuckDuck 2")
else:
    print("DuckDuck 1")