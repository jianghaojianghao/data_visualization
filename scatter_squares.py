# JiangHao
import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

#edgecolors: deleting the color of outline
# plt.scatter(x_values,y_values,c='red',edgecolors='none',s=50)
# plt.scatter(x_values,y_values,c=(0, 0, 0.8),edgecolors='none',s=50)
plt.scatter(x_values,y_values,c=y_values,edgecolors='none',s=50,cmap=plt.cm.Blues) #colormap 颜色映射


plt.axis([0, 1100, 0, 1100000])

#title
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#tick mark
plt.tick_params(axis='both',which='major',labelsize=14)

#If you want to disable both the offset and scientific notaion,
# you'd use ax.ticklabel_format(useOffset=False, style='plain').
plt.ticklabel_format(useOffset=False, style='plain')

plt.show()

#save graph, bbox_inches: whether cutting redundant white space
# plt.savefig('squares_plot.png', bbox_inches='tight')