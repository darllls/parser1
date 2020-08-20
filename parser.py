import requests
from bs4 import BeautifulSoup

def parse():
    url = 'https://www.olx.ua/uk/zhivotnye/koshki/'
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'
    }
   
    req = requests.get(url, headers = headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    items = soup.findAll('div', class_ = 'offer-wrapper')
    elements = []
    try:
        for item in items:
            elements.append({
                'title' : item.find('a', class_ = 'marginright5 link linkWithHash detailsLink').get_text(strip=True),
                'link' : item.find('a', class_ = 'marginright5 link linkWithHash detailsLink').get('href')
            })
    except Exception as e:
        pass
        #print(str(e))

    global element
    for element in elements:
        print(f'{element["title"]} ->  Link: {element["link"]}')
       

def save():
    with open('parser_info.txt','a') as file:
        file.write(f'{element["title"]} ->  Link: {element["link"]}')


parse()
save()