# JiangHao
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 使用颜色映射来指出漫步中各点的先后顺序，并删除每个点的黑色轮廓
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=100)

    # 隐藏坐标轴
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    # 设置绘图窗口的尺寸 单位为英寸
    plt.figure(dpi=128, figsize=(10, 6))

    plt.show()

    keep_runnning = input('Make another walk? (y/n): ')
    if keep_runnning == 'n':
        break