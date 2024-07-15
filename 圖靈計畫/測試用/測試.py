#4 Taiko Time
def calculate_score(input_data):
    from math import floor
    import numpy as np

    # 解析输入数据
    lines = input_data.strip().split('\n')
    N, M, W, K = lines[0].split()
    N, M, K = int(N), int(M), int(K)
    W = float(W)

    note_times = list(map(int, lines[1].split()))
    note_types = list(lines[2].strip())
    hit_times = list(map(int, lines[3].split()))
    hit_types = list(lines[4].strip())

    kiai_intervals = []
    for i in range(K):
        start, end = map(int, lines[5 + i].split())
        kiai_intervals.append((start, end))

    # 计算判定时间范围
    GREAT = floor(50 + 50 * (W - 5) / 5)
    OK = floor(100 + 100 * (W - 5) / 5)
    MISS = floor(150 + 150 * (W - 5) / 5)
    #print(GREAT, OK, MISS)

    num_great = 0
    num_ok = 0
    num_miss = 0

    b = [[] for _ in range(len(note_times))]  # 初始化一个空列表的列表
    min_diff_indices = []
    min_diff = []
    min_diff_indices_ = []

    for i in range(len(note_times)):
        for j in range(len(hit_times)):
            b[i].append(np.abs(note_times[i] - hit_times[j]))

        min_diff_value = min(b[i])
        min_diff.append(min_diff_value)
        min_diff_indices.append(b[i].index(min_diff_value))

        #print(min_diff_indices_,min_diff_indices)
        if min_diff_indices[i-1] == None:
            print(min_diff_indices[i],0)

            min_diff_indices_.append(min_diff_indices[i]-0)
        else:
            print(min_diff_indices[i],min_diff_indices[i-1])

            #min_diff_indices_.append(min_diff_indices[i]-min_diff_indices[i-1])

    print(min_diff_indices, min_diff,min_diff_indices_)



    # 生成结果列表
    results = [''] * len(note_times)
    for i in range(len(min_diff)):
        if hit_types[min_diff_indices[i]] != note_types[i]:
            results[i] = 'MISS'
            num_miss += 1
        elif min_diff[i] < GREAT:
            results[i] = 'GREAT'
            num_great += 1
        elif min_diff[i] <= OK:
            results[i] = 'OK'
            num_ok += 1
        else:
            results[i] = 'MISS'
            num_miss += 1

    print(results)
    b = 1

    for i in range(len(min_diff_indices)):
        print(i+b,min_diff_indices[i])
        if min_diff_indices[i] != i+b:
            results[i] = 'MISS'
            b+=1
            num_miss+=0.5
            num_great-=0.5
    print(results)

    # 计算分数
    total_score = 0
    current_combo = 0
    max_combo = 0
    for i in range(N):
        note_time = note_times[i]
        judgment = results[i]
        basic_score = 0
        print

        if judgment == 'GREAT':
            basic_score = 300
            print('i')
            current_combo += 1
        elif judgment == 'OK':
            basic_score = 150
            current_combo += 1
        else:
            current_combo = 0

        multiplier = 1
        if kiai_intervals[0][0]<note_time<kiai_intervals[0][1] or kiai_intervals[0][0]==note_time or kiai_intervals[0][1]==note_time:
            multiplier = 1.2

        combo_factor = max(1, current_combo // 10)
        note_score = basic_score * multiplier * combo_factor
        total_score += note_score

        max_combo = max(max_combo, current_combo)

    # 计算准确率
    accuracy = (num_great + num_ok / 2) / N * 100
    accuracy = round(accuracy, 2)

    # 输出结果
    print(total_score)
    print(int(num_great), int(num_ok), int(num_miss))
    print(f'{accuracy:.2f}')
    print(max_combo)

# 测试
input_data1 = """7 8 5 1
200 400 600 1000 1100 1450 2434
DDKKDKK
100 106 200 399 650 1050 1116 1488
DDDDKKDD
400 1000"""

calculate_score(input_data1)