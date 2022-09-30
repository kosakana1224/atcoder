from matplotlib import pyplot as plt
from random import randint

# データの定義(サンプルなのでテキトー)
x = list(range(10))
y1 = [randint(0, 100) for _ in x]
y2 = [randint(0, 100) for _ in x]

# グラフの描画
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()