from pyecharts import GeoLines, Style


# add(name, data,
#     maptype='china',
#     symbol=None,
#     symbol_size=12,
#     border_color="#111",
#     geo_normal_color="#323c48",
#     geo_emphasis_color="#2a333d",
#     geo_cities_coords=None,
#     geo_effect_period=6,
#     geo_effect_traillength=0,
#     geo_effect_color='#fff',
#     geo_effect_symbol='circle',
#     geo_effect_symbolsize=5,
#     is_geo_effect_show=True,
#     is_roam=True, **kwargs)


# 默认效果
style = Style(
    title_top='#fff',
    title_pos='center',
    width=1200,
    height=600,
    background_color='#404a59'
)

# data_guangzhou = [
#     ["广州", "上海"],
#     ["广州", "北京"],
#     ["广州", "南京"],
#     ["广州", "重庆"],
#     ["广州", "兰州"],
#     ["广州", "杭州"]
# ]
# 指定数值
data_guangzhou = [
    ["广州", "上海", 10],
    ["广州", "北京", 20],
    ["广州", "南京", 30],
    ["广州", "重庆", 40],
    ["广州", "兰州", 50],
    ["广州", "杭州", 60],
]
# 多例模式
data_beijing = [
    ["北京", "上海"],
    ["北京", "广州"],
    ["北京", "南京"],
    ["北京", "重庆"],
    ["北京", "兰州"],
    ["北京", "杭州"]
]

# 稍加配置
style_geo = style.add(
    is_label_show=True,
    line_curve=0.2,
    line_opacity=0.6,
    legend_text_color="#eee",
    legend_pos="right",
    geo_effect_symbol="plane",
    geo_effect_symbolsize=15,
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#eee",
)
# 单例模式，指定
style_geo = style.add(
    is_label_show=True,
    line_curve=0.2,
    line_opacity=0.6,
    legend_text_color="#eee",
    legend_pos="right",
    geo_effect_symbol="plane",
    geo_effect_symbolsize=15,
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#eee",
    legend_selectedmode="single", #指定单例模式
)
geolines = GeoLines("GeoLines 示例", **style.init_style)
# geolines.add("从广州出发", data_guangzhou, is_legend_show=False)
# geolines.add("从广州出发", data_guangzhou, **style_geo)
geolines.add("从广州出发", data_guangzhou,tooltip_formatter="{a}:{c}" ,**style_geo)
geolines.add("从广州出发", data_beijing, **style_geo)
geolines.render()


