from urllib.request import urlopen

from django.shortcuts import render_to_response

import os
from sys import stdout


import json
import threading
import time
import random
import binascii
import facebook

class MyThreading(object):


    def __init__(self):

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        self.stop = False

    def run(self,request):
        while True:
            def post():
                string = str(binascii.hexlify(os.urandom(20)))
                list = [
                    'Total signatures till now is ',
                    'The latest result of the petition is ',
                    'Till now the number of collected signatures is '
                ]
                ran = random.choice(list)
                message = string + ' Ignore this. \n' + ran + str(get_data())
                auth = request.user.social_auth.first()
                if not auth:
                    stdout.write('User %s is not authenticated with Facebook' % request.user)
                    return
                graph = facebook.GraphAPI(auth.extra_data['access_token'])
                graph.put_object("me", "feed", message=message)
            post()
            time.sleep(60)
            if self.stop:
                return




thread = MyThreading()

def get_data():
    url = "https://petition.parliament.uk/petitions/206568.json"
    response = urlopen(url)
    data = response.read().decode("utf-8")
    dict = json.loads(data)
    total = dict['data']['attributes']['signature_count']
    return total

def index(request):
    thread.stop = True
    context={
        'request':request,
        'user':request.user
    }
    return render_to_response('petition/index.html', context)
    #return HttpResponse(total)

def done(request):
    thread.stop=False
    thread.run(request)
    return render_to_response('petition/done.html', context={})

'''def stop(request):
    context = {
        'request': request,
        'user': request.user
    }
    thread.__exit__()
    return render_to_response('petition/index.html', context={})

'''
def home(request):
   context ={
       'request':request,
       'user': request.user
   }
   return render_to_response('petition/homepage.html', context)




