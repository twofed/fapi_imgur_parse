from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from lxml import html
import uvicorn
import requests
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")
defpage = 'https://imgur.com'

@app.get("/imgur/html/{searchword}", response_class=HTMLResponse)
async def get_imgur_html(request: Request, searchword: str):
    json_data = searchimgur(searchword)
    return templates.TemplateResponse("imgursearch.html", {"request": request, "json_data": json_data})

@app.get("/imgur/json/{searchword}")
async def get_imgur_json( searchword: str):
    json_data = searchimgur(searchword)
    return json_data

def searchimgur(searchword,pagecount=1):
    curentpage = 0
    result = []
    while curentpage!=pagecount:
        print('page :',curentpage+1)
        page = requests.get('https://imgur.com/search?q='+searchword+'&p='+str(curentpage+1))
        searchpage = html.fromstring(page.content)
        elem = searchpage.xpath("//a[@class='image-list-link'][1]/@href")
        for el in elem:
            subpage = requests.get(defpage+el)
            subparse = html.fromstring(subpage.content)
            scriptel = subparse.xpath('//script')[0].text
            jsondata = scriptel.split('window.postDataJSON="')[1]
            try:
                qwe= json.loads(jsondata[:-1].replace("\\",''))
                result.append(qwe)
            except:
                print('false parse')
        curentpage+=1
    return(result)

# if __name__ == '__main__':
#     uvicorn.run('main:app', host='0.0.0.0', port=8000)

