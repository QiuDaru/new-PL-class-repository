#輸入
n,k = list(map(int,input().split()))
# c = 0 ~ k
all_data =[]
c_data0 = []  #初始為零   0,1
c_data1 = []#初始為一   2 
ans = []
shunsh = [] 
for _ in range(n):
    all_data.append(list(map(int, input().split())))
for i in range(k):
    if i <= int(all_data[0][1]) :
        c_data0.append(i)
        shunsh.append(0) 

    if i > int(all_data[0][1]) :
        c_data1.append(i)
        shunsh.append(1)

def z(t,s,data0,k):#初始為零 # t=3 s=2 data0=0 k=3 
    n = k-data0 # -0 =3 # 時間差 = 3
    print("起始:0","t:",t,"s",s,'data0',data0,"k",k)
    if n == 0:
        return 0
    
    if (t-data0)%n == 0 :
        return 1
    else:
        return 0 
    

def o(t,s,data1,k):
    print("起始:1","t:",t,"s",s,'data1',data1,"k",k)
    n = k-data1-1
    if n == 0 :
        return 1

    if (t-data1)%n == 0 :
        return 1
    else:
        return 0 
print("============")
print("1"*k)

for _ in range(n):
    
    ans = []
    for i in range(k):
        t =all_data[i+1][0]
        
        s =all_data[i+1][1]
    
        k1 = k


        if shunsh[i] == 0 :

            for0 = 0
            for1 = 0
            for i in range(len(c_data0)):
                data0 = c_data0[for0]
                for0 = for0+1
                ans.append(z(t,s,data0,k1))
            
                print(z(t,s,data0,k1))
        if shunsh[i] == 1:

            for0 = 0
            for1 = 0
            for i in range(len(c_data1)):
                data1 = c_data1[for1]
                for1 = for1+1
                ans.append(o(t,s,data1,k1))
                print(o(t,s,data0,k1))

    print("ans",ans)








