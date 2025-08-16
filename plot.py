import matplotlib.pyplot as plt
import datetime
import os

# 確保資料夾存在
os.makedirs("docs/images", exist_ok=True)

# 生成示例圖
now = datetime.datetime.now()
plt.figure(figsize=(6,4))
plt.plot([1,2,3,4,5], [5,4,3,2,1], marker='o')
plt.title(f"自動更新圖 - {now.strftime('%Y-%m-%d %H:%M:%S')}")
plt.xlabel("X")
plt.ylabel("Y")

# 儲存圖片
plt.savefig("docs/images/output.png")
plt.close()
