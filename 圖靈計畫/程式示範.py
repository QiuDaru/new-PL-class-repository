#撲克之王安妮亞
x = int(input("請輸入x:"))
first = 0
s = 1
#  x = 5個數字的加總，x = 5 ~ 65
for i in range(13):  # 找出前面4個一樣的數字
    first = first+1
    
    for i in range(13):# 最後一個數字
        if first*4 + s == x:
            print(first,first,first,first,s)
            exit()
        s = s+1
        
        





