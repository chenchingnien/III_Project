import requests
# from urllib.request import urlopen
from bs4 import BeautifulSoup
from CrawlerDemo105.CB105_G4_Project import defmeta
import re
import pandas as pd
# from requests_html import HTML

#  import warnings
#  warnings.filterwarnings("ignore")

jar = requests.cookies.RequestsCookieJar()
jar.set("over18", "1", domain="www.ptt.cc")

#  WomenTalk版首頁開
url = "https://www.ptt.cc/bbs/ALLPOST/index.html"

#  準備記錄表格
df = pd.DataFrame(columns=["作者", "看板", "標題", "時間", "分數", "內容"])


#  走過10頁產生一個list
for times in range(10):
    #  send a request and fetch the web page從WomenTalk版首頁開始搜尋玫瑰關鍵字
    search_endpoint_url = 'https://www.ptt.cc/bbs/Plant/search'
    response = requests.get(search_endpoint_url, cookies=jar, params={'q': '玫瑰花'}).text
    html = BeautifulSoup(response.txt, 'lxml')
    #  print(html)

    # 得到每一篇文章區域
    # 使用find_all()找尋特定目標
    articles = html.find_all("div", class_="r-ent")
    # print(articles)

    # 走過每一篇文章
    for single_article in articles:
        # 得到 title 的超連結元素 <a>
        # score_area = single_article.find("div", class_="nrec").find("span")
        title_area = single_article.find("div", class_="title").find("a")
        # meta_area = single_article.find("div", class_="meta").find("div", "date")
        # print(title_area)
        # 如果有 title 才繼續 (被刪除的文章會沒有 title)
        if title_area:
            # 得到 title 的文字
            title = title_area.contents[0]
            # 得到 title 的超連結屬性 href
            article_url = "https://www.ptt.cc/" + title_area["href"]
            # 使用我們剛剛定義的函式
            result = defmeta.get_page_meta(article_url)
            # print(article_url)
            # 檢查是不是回傳 None(公告和版規會回傳 None)
            if result:
                data = [result["author"], result["board"], result["title"], result["time"], result["score"],
                        result["content"]]
                c = ["作者", "看板", "標題", "時間", "分數", "內容"]
                s = pd.Series(data, index=c)
                df = df.append(s, ignore_index=True)
    #  往下一頁前進, string參數可以找裡面文字符合我們帶入字串的元素
    url = html.find("a", text=re.compile(r"上頁"))["href"]
#df.to_csv("ALLPOST.csv", index=False, encoding="utf-8")
print(df)
