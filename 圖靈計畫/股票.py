# 初始化變數
X = 0  # 一開始買股的錢
N = 0  # 季度數量
G = 0  # 股息
H = 0  # 總花費

# 輸入季度數量和買進價格
while True:
    y = list(map(int, input("請輸入季度與買進價格，用空格分隔: ").split()))
    if len(y) == 2:
        break
    else:
        print("請確保輸入兩個整數值，分別表示季度數量與買進價格。")
N, X = y

# 輸入每個季度的股價
m = list(map(int, input("請輸入每個季度的股價，用空格分隔: ").split()))

# 計算總花費和股息
H += X
for A in m:
    G += A / 100
    if G >= A:
        G -= A
        H += A


        

# 判斷獲利還是虧損
if H > X:
    print("stonks")
else:
    print("NOT stonks")
