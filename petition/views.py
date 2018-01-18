from django.shortcuts import render
from urllib.request import urlopen
from django.http import HttpResponse
import json
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def get_jsonparsed_data(request):
    url = "https://petition.parliament.uk/petitions/206568.json"
    response = urlopen(url)
    data = response.read().decode("utf-8")
    dict=json.loads(data)
    total=dict['data']['attributes']['signature_count']

    return HttpResponse(total)



def home(request):
   context ={
       'request':request,
       'user': request.user
   }
   return render_to_response('petition/homepage.html', context)
