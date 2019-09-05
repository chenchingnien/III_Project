import requests
from bs4 import BeautifulSoup
title = str()

def get_page_meta(url):
    jar = requests.cookies.RequestsCookieJar()
    jar.set("over18", "1", domain="www.ptt.cc")

    # 先做最基礎的判斷, 非公告和版規我回傳答案
    if not "公告" in title and not "版規" in title:
        response = requests.get(url, cookies=jar).text
        html = BeautifulSoup(response)
        content = html.find("div", id="main-content")
        # 準備我們要回傳的字典
        result = {}
        values = content.find_all("span", class_="article-meta-value")
        # 先把文章資訊記錄在字典裡
        result["author"] = values[0].text
        result["board"] = values[1].text
        result["title"] = values[2].text
        result["time"] = values[3].text
        meta = content.find_all("div", class_="article-metaline")
        for m in meta:
            m.extract()
        right_meta = content.find_all("div", class_="article-metaline-right")
        for single_meta in right_meta:
            single_meta.extract()
        pushes = content.find_all("div", class_="push")
        score = 0
        for single_push in pushes:
            pushtag = single_push.find("span", class_="push-tag").text
            if "推" in pushtag:
                score = score + 1
            elif "噓" in pushtag:
                score = score - 1
            single_push.extract()
        # 分數和內容
        result["score"] = score
        result["content"] = content.text
        return result
        # 公告和版規我就直接回傳 None
    else:
        return None


