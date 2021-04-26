from random import randrange

from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Bar
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))


app = Flask(__name__, )


# pyecharts 的图 上传到html中
def bar_base() -> Bar:
    c = (
        Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
            .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c


from pyecharts.charts import WordCloud


def WordCloudPic():
    data = [('ネイルマシン', '41'),
            ('ネイルマシーン', '40'),
            ('ネイル マシン', '35'),
            ('ネイルケア 電動', '33'),
            ('電動ネイルケア', '29'),
            ('ネイル 電動', '28'),
            ('ネイル マシーン', '27'),
            ('ネイルマシーン 電動ネイルマシン', '20'),
            ('ネイルドリル', '20'),
            ('爪やすり 電動', '20'),
            ('ネイルケア', '19'),
            ('つめやすり 電動', '15'),
            ('ネイルオフマシーン', '15'),
            ('stargreen', '13'),
            ('ネイルケアセット', '10'),
            ('爪 やすり 電動', '9'),
            ('電動つめやすり', '8'),
            ('ネイルケア セット', '7'),
            ('ネイルオフ', '7'),
            ('ジェルネイル オフ 電動', '7'),
            ('ネイル ケア', '6'),
            ('爪 電動', '6'),
            ('電動爪やすり', '6'),
            ('ネイル オフマシーン', '6'),
            ('爪 やすり おすすめ 電動', '5'),
            ('つめみがき 電動', '5'),
            ('甘皮処理 電動', '5'),
            ('電動 ネイル', '4'),
            ('ネイルケアキット', '4'),
            ('電動ネイルマシン', '4'),
            ('電動 爪 ヤスリ', '3'),
            ('ネイルマシン 電動ネイルケア', '3'),
            ('電動 爪 やすり', '3'),
            ('電動ネイル', '3'),
            ('ネイルケアマシン', '3'),
            ('ネイル やすり 電動', '3'),
            ('爪けずり 電動', '2'),
            ('ネイルケアセット 電動', '2'),
            ('ネイルオフマシン', '2'),
            ('爪ヤスリ 電動', '2'),
            ('電動式ネイルケア', '2'),
            ('ネイルけあセット', '2'),
            ('電動ネイルケアセット', '2'),
            ('ネイル オフ マシーン', '1'),
            ('ネイルましーん', '1'),
            ('プチトル ネイルマシン', '1'),
            ('プチトル', '1'),
            ('nail care set', '1'),
            ('ネイルオフ マシン', '1'),
            ('美甲', '1'),
            ('ネイルマシン プロ用', '1'),
            ('電動爪 やすり', '1'),
            ('ネイルケア 甘皮', '1'),
            ('爪ケアセット', '1'),
            ('ネイル オフ', '1'),
            ('ネイルケア 電動 ランキング', '1'),
            ('nail', '1'),
            ('ネイル ケア セット', '1'),
            ('ネイルケア マシン', '1')]
    c = (
        WordCloud()
            .add(series_name="关键词分析", data_pair=data, word_size_range=[6, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="关键词-热点分布", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    return c



@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()

@app.route("/")
def index():

    c2 = bar_base()  # pyecharts 画图
    c = WordCloudPic()  # pyecharts 画图

    return render_template("index.html",
                           Bar2_options=c2.dump_options_with_quotes(), # 柱状图
                           Bar3_options=c2.dump_options(),        #
                           Cloud_options=c.dump_options(),      #  词云图

                           )


if __name__ == "__main__":
    app.run(debug=True)
