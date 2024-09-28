def can_contain(box, bocchi):
    box_sorted = sorted(box)  # 排序
    bocchi_sorted = sorted(bocchi)
    return all(box_dim >= bocchi_dim for box_dim, bocchi_dim in zip(box_sorted, bocchi_sorted))  # 检查每个箱子的尺寸是否能容纳波奇

def main():
    data = input().split()

    n = int(data[0])  #箱子數
    boxes = []
    index = 1  # 零是箱子数量
    for i in range(n):
        l, w, h = int(data[index]), int(data[index + 1]), int(data[index + 2])  # 箱子长宽高
        boxes.append((l, w, h))
        index += 3

    bocchi = (int(data[index]), int(data[index + 1]), int(data[index + 2]))  # 波奇长宽高

    count = 0
    for box in boxes:
        if can_contain(box, bocchi):
            count += 1  # 有几个箱子可以容纳波奇

    print(count)

if __name__ == "__main__": #沒什麼用的一行
    main()