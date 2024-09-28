def check_stamina(n, t, checks):
    for i, (minute, stamina) in enumerate(checks):
        possible_r = ['1'] * t
        for r in range(t):
            # 计算体力值增加的总量
            gained_stamina = (minute - r + t) // t
            if not ((minute % t == r and gained_stamina == stamina) or (minute % t != r and gained_stamina - 1 == stamina)):
                possible_r[r] = '0'
        print("".join(possible_r))

# 从输入中读取数据
n, t = map(int, input().split())
checks = [tuple(map(int, input().split())) for _ in range(n)]

check_stamina(n, t, checks)
