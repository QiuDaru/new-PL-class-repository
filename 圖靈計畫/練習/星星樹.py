#星星數
n= int(input())
nai = list(map(int,input().split()))
nai_ans = 0
x = len(nai)
for i in range(x):
    nai_ans=nai[i]+nai_ans
    print(nai_ans)


qt = int(input())

for i in range(qt):
    qt_ans = 0
    x1,x2 = list(map(int,input().split()))
    for i in range(x1-1,x2):
        qt_ans =nai[i]+qt_ans
    print(qt_ans)












