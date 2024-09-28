l = []
ans =[]
ans1 = []
trn, hn = list(map(int, input().split()))
if hn<3 or trn<3 : 
    print("-1")
for i in range(trn):
    l+=list(map(int, input().split()))

if len(l)/trn!=hn:
    print("-1")
for i in range(trn):
    y=[]
    for y in range(hn): 
            ans += max[y]
print(ans)