# JiangHao
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取日期、最高气温和最低气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 打印每列代表的意思
    # for index,column in enumerate(header_row):
    #     print(index,column)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            #只要缺失其中一项数据，Python就会引发ValueError异常
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
#alpha 指定颜色的透明度。Alpha 值为0表示完全透明，1(默认设置)表示完全不透明
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
#向fill_between() 传递了一个 x 值系列:列表dates ，还传递了两个 y 值系列:highs 和lows
#实参facecolor 指定了填充区域的颜色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high temperatures, 2014\nDeath Valley, CA", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() #绘制斜的日期标签，以免它们彼此重叠
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()