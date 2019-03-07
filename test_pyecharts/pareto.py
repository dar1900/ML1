import pandas as pd

data = pd.read_excel('catering_dish_profit.xls', index_col=u'菜品名')
data = data[u'盈利'].copy()
data.sort_values(ascending=False)  # 排序

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
data.plot(kind='bar')
plt.ylabel(u'盈利（元）')

p = data.cumsum() / data.sum()
p.plot(color='r', secondary_y=True, style='-o', linewidth=2)
plt.annotate(format(p[6], '.4%'), xy=(6, p[6]), xytext=(6 * 0.9, p[6] * 0.9),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'))
plt.ylabel(u'盈利（比例）')
plt.ylim(0, 1.1)

plt.show()
