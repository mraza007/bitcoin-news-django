from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
import json
# Init
newsapi = NewsApiClient(api_key='XXXXXXXXXXXXXXX')
all_articles = newsapi.get_everything(q='bitcoin',sources='yahoo,the-verge,cnbc,bloomberg',domains='bbc.co.uk,techcrunch.com',language='en',sort_by='relevancy')
new = json.dumps(all_articles)
data = json.loads(new)
def index(request):
    return render(request,'news/index.html',{'data':data})