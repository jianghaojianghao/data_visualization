# JiangHao
import json
import pygal
from pygal.style import RotateStyle, LightColorizedStyle

from country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as file:
    #函数json.load() 将数据转换为Python能够处理的格式,这里是一个列表
    pop_data = json.load(file)

# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        #Python不能直接将包含小数点的字符串'1127437398.85751' 转换为整数
        #这个小数值可能是人口数据缺失时通过插值得到的
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            '''
            导致显示错误消息的原因有两个。首先，并非所有人口数量对应的都是国家，有些人口数量对应的是地区(阿拉伯世界)
            和经济类群(所有收入水平)。其次，有些统计数据使 用了不同的完整国家名(如Yemen, Rep.，而不是Yemen)。
            '''
            print('Error-'+country_name)
# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop <1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))


# 制作世界地图
# Pygal样式存储在模块style 中，我们从这个模块中导入了样式RotateStyle。
# 创建这个类的实例时，需要提供一个实参——十六进制的RGB颜色(见❷);Pygal将根 据指定的颜色为每组选择颜色。
# LightColorizedStyle 加亮了地图的颜色
wm_style = RotateStyle('#336699',base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('americas.svg')