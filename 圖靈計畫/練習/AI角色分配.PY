def permute(arr, l, r, result):
    if l == r:
        result.append(arr[:])
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]
            permute(arr, l + 1, r, result)
            arr[l], arr[i] = arr[i], arr[l]

def role_assignment(test_cases):
    results = []
    positions = ['JG', 'MID', 'TOP', 'SUP', 'AD']
    for case in test_cases:
        players = case
        possible_permutations = []
        permute(positions, 0, len(positions) - 1, possible_permutations)
        valid_assignments = 0
        
        for perm in possible_permutations:
            valid = True
            for i, pos in enumerate(perm):
                if pos not in players[i]:
                    valid = False
                    break
            if valid:
                valid_assignments += 1
                
        results.append(valid_assignments)
    return results

# 讀取輸入數據
t = int(input())
test_cases = []
for _ in range(t):
    players = []
    for _ in range(5):
        data = input().split()
        p = int(data[0])
        positions = data[1:]
        players.append(positions)
    test_cases.append(players)

# 計算並輸出結果
results = role_assignment(test_cases)
for result in results:
    print(result)
