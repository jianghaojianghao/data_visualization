# JiangHao
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS, Style


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
#响应对象包含一个名为status_code 的属性，它让我们知道请求是否成功了(状态码200表示请求成功)
# 倘若GitHub 无法全面处理该API，incomplete_results 这个值将为true
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
#使用方法json() 将这些信息转换为一个Python字典
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# for repo_dict in repo_dicts:
#     print("\nSelected information about first repository:")
#     print('Name:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Created:', repo_dict['created_at'])
#     print('Updated:', repo_dict['updated_at'])
#     print('Description:', repo_dict['description'])

# 研究仓库
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dicts.append({
      'value': repo_dict['stargazers_count'],
      'label': repo_dict['description'],
      'xlink': repo_dict['html_url'], #Pygal根据与键'xlink' 相关联的URL将每个条形都转换为活跃的链接
    })

# 可视化
# 通过修改my_config 的属性，可定制图表的外观
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
# 让标签绕x 轴旋转45度
my_config.x_label_rotation = 45
# 隐藏了图例
my_config.show_legend = False
# 主标签是 y 轴上为5000整数倍的刻度;这些标签应更大，以与副标签区分开来
# 用truncate_label 将较长的项目名缩短为15个字符(如果你将鼠标指向屏幕上被截短的项目名，将显示完整的项目名)
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

# 让标签绕x 轴旋转45度 (x_label_rotation=45 )，并隐藏了图例(show_legend=False )
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

custom_style = Style(
  background='transparent',
  plot_background='transparent',
  foreground='#53E89B',
  foreground_strong='#53A0E8',
  foreground_subtle='#630C0D',
  opacity='.6',
  opacity_hover='.9',
  transition='400ms ease-in',
  colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'),
  major_label_font_size=18,
  label_font_size=14,
  title_font_size=24
)

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

# 由于我们不需要给这个数据系列添加标签，因此在此处添加数据时，将标签设置成了空字符串
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
