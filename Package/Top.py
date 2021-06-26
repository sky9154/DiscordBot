import requests
import json

def Top(number):
    if number>20:
        return("請輸入20以下的數字")
    else:
        n=1
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',  
        }

        params = {
            'hl': 'zh-TW', #繁體中文，hl > Language to return result headers in
            'tz': '-480', #時區，tz > Timezone using Etc/GMT
            'geo': 'TW', #地區，geo > two letter country abbreviation
        }

        url = 'https://trends.google.com.tw/trends/api/dailytrends'
        response = requests.get(url, headers=headers, params=params)

        json_str = response.text[5:] #刪去雜訊
        j_dic = json.loads(json_str) #將str轉成dict

        #分析json檔
        #trendingSearchesDays > 搜尋日期。[0]為今天，[1]為昨天
        #trendingSearches > 關鍵字。
        topics = j_dic['default']['trendingSearchesDays'][0]['trendingSearches']
        data = ''
        for i, topic in enumerate(topics):
            if i < number:
                data += '第%s名關鍵字: '%(n) + topic['title']['query'] + '\n'
                data += '搜索量: ' + topic['formattedTraffic'] + '\n'
                data += '文章:' + topic['articles'][0]['title'] + '\n'
                data += '連結:' + topic['articles'][0]['url'] + '\n'
                data += '-------------------------\n'
                n+=1
        return(data)