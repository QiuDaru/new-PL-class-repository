n,t1,t2 = list(map(int,input().split()))
t_t = t1-t2
t_t= abs(t_t)
ans = 0
tb = 0
#print((n-t1),(t1-1),(t2-1),(n-t2))


if ((n-t1 or t1-1) < (t2-1)) and ((n-t1 or t1-1) <(n-t2)):

    if n-t1>t1-1:
        tb = t1-1
    else:
        tb = n-t1 


else:

    if n-t2>t2-1:

        tb = t2-1
    else:

        tb = n-t2 


if t_t % 2==0:
    ans = t_t//2


else:
    ans = t_t//2+tb

    ans = ans+1

print(ans)

