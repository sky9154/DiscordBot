import urllib.request
import urllib.parse
import json
def v(query,limit):
    url = 'https://api.avgle.com/v1/search/{}/{}?limit={}'
    query=query
    limit=limit
    page = 1
    resp = json.loads(urllib.request.urlopen(url.format(urllib.parse.quote_plus(query), page, limit)).read().decode())
    videos = resp['response']['videos']
    video=dict(videos[0])
    return(video['title'],video['video_url'],video['preview_url'])