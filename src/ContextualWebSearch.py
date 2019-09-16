import requests

def get_news(api_key ):
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI"
    querystring = {
        "autoCorrect":"false",
        "pageNumber":"1",
        "pageSize":"100",
        "safeSearch":"false"
    }
    headers = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
#    print(response.text)
    return response.text
def run():
    try:
        out_file = '/tmp/work/contextualwebsearch_news.json'
        api_key = None
        with open('/home/pi/root/work/record/pc/account/rapidapikey', mode='r') as f:
            api_key = f.read().strip();
#        print(api_key)
        with open(out_file , mode='x', encoding='utf-8') as f:
            f.write(get_news(api_key));
    except FileExistsError: print('出力ファイルが既存のため中止する。\n' + out_file)

run()

