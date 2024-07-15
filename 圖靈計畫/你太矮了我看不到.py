N = int(input())
p = list(map(int,input().split()))
n = 0
g =[]
g.append(p[0])
for i in range(N-1):
    if p[n]== p[n+1]:
        g.append(1)

    else:
        g.append(p[n+1])
    n=n+1
print(g)