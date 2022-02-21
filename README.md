# fapi_imgur_parse
FastAPI Search and Scraping Images from Imgur

Methods:
```
GET
/imgur/html/{searchword}
```
Return Html Search result page

```
GET
/imgur/json/{searchword}
```
Return Json Search result 

Sample:
```
http://127.0.0.1:80/imgur/html/cat
```
![alt text](https://i.imgur.com/Gug7bHw.png)
