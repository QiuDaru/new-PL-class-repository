def game_stamina(n, m, checks):
    possible_remainders = set(range(m))  # 初始化所有可能的餘數
    
    for t, s in checks:
        new_possible_remainders = set()
        
        for r in possible_remainders:
            # 計算檢查時間 t 分鐘前可能的體力值
            possible_stamina = (t - r) // m
            
            if possible_stamina * m + r == t:
                new_possible_remainders.add(r)
        
        possible_remainders = new_possible_remainders
        result = ''.join('Y' if i in possible_remainders else 'N' for i in range(m))
        print(result)

# 範例輸入
n = 3
m = 5
checks = [(5, 2), (10, 4), (15, 6)]

# 呼叫函數
game_stamina(n, m, checks)
