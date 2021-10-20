import requests
import json

def Top(number):
    n = 1
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",  
    }

    params = {
        "hl": "zh-TW", # 繁體中文，hl > Language to return result headers in
        "tz": "-480", # 時區，tz > Timezone using Etc/GMT
        "geo": "TW", # 地區，geo > two letter country abbreviation
    }

    url = "https://trends.google.com.tw/trends/api/dailytrends"
    response = requests.get(url, headers=headers, params=params)

    json_str = response.text[5:] # 刪去多於字元
    j_dic = json.loads(json_str) # 將 str 轉成 dict


    topics = j_dic["default"]["trendingSearchesDays"][0]["trendingSearches"]
    data = ">>> "
    for i, topic in enumerate(topics):
        if i < number:
            data += "**第 %s 名關鍵字: **"%(n) + topic["title"]["query"] + "\n"
            data += "**搜索量: **" + topic["formattedTraffic"] + "\n"
            data += "**文章: **" + topic["articles"][0]["title"] + "\n"
            data += "**連結: **" + topic["articles"][0]["url"] + "\n"
            data += "----------------------------------------\n"
            n+=1
    return(data)