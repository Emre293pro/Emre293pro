
from flask import Flask
import random

app = Flask(__name__)

facts_list = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar",
              "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor",
              "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
              "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
              "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır."]

komik_list = ["https://www.youtube.com/watch?v=8C_wVex0q7s&pp=ygUOa29taWsgdmlkZW9sYXI%3D",
              "https://www.youtube.com/shorts/fItwAHNTN0k",
              "https://www.youtube.com/watch?v=JrjDDf1S68M&pp=ygUNYW5uZSB0ZXJsacSfaQ%3D%3D"]

yazı_tura = ["yazı mı tura mı?","şaka yaptım  burası çizgi roman yeri","sana bir çizgi roman köpek adam!https://youtu.be/Q2btiI9a31g"]

@app.route("/")
def index():
    return f"<h1>merhaba, bu sayfada ilginç bir gerçeklik bulacaksın, eğer /2 yazarsan süpriz sayfa! </h1> <a href='/rastgele_gercek'> bana tıkla!</a> "

@app.route("/rastgele_gercek")
def index2():
    return f"<p> {random.choice(facts_list)}  </p>"

@app.route("/2")
def index3():
    return f"<h1>hangi oyunu istersiniz? Yazı tura için yan çizgi (/) ile yazı_tura yazın komik viedo için komik_youtube yazın <h1> <a href='/yazı_tura'> yazı tura!</a> <h1> <a href='/komik_youtube'> komik youtube!</a>  "

@app.route("/yazı_tura")
def index4():
    return f"<p> {random.choice(yazı_tura)}  </p>"

@app.route("/komik_youtube")
def index5():
    return f"<p> {random.choice(komik_list)}  </p>"



app.run(debug=True)
