import pandas as pd
import matplotlib.pyplot as plt

# 提供文件的完整路径
file_path = "Pandas練習\心理健康問卷3.0 (回覆) - 表單回應 1.csv"
data = pd.read_csv(file_path, encoding="utf-8")
print(data.index)
a = data.plot(x="我這一周內覺得頭暈或胸悶",y="您的年齡是?",kind="line")
plt.show()
