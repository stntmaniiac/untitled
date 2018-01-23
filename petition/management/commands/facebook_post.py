from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.http import HttpResponse
from social_django.models import UserSocialAuth
from urllib.request import urlopen
import binascii
import webbrowser
import os
import random
import time
import facebook
import json
import tweepy
class Command(BaseCommand):
    args = ''
    help = 'Posts a message to Facebook'

    def get_data(self):
        url = "https://petition.parliament.uk/petitions/206568.json"
        response = urlopen(url)
        data = response.read().decode("utf-8")
        dict = json.loads(data)
        total = dict['data']['attributes']['signature_count']
        return total

    def get_api(self, cfg):
        auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
        auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
        return tweepy.API(auth)

    def handle(self, *args, **options):
        user = UserSocialAuth.objects.get(provider='facebook', )
        if user is None:
            url = 'http://localhost:8000'
            webbrowser.open(url)
            while not user:
                user = UserSocialAuth.objects.filter(provider='facebook').first()
                time.sleep(2)

        self.stdout.write('User authenticated')
        self.stdout.write(user.uid)


        #twitter credentials
        cfg = {
            "consumer_key": "o6czyLePr7BbUlQQhqiFHzVyc",
            "consumer_secret": "6Q1rj3pJa2rkZ4ea3v5rX7DFFtk4274njqbX3abBH2kAR2BjLT",
            "access_token": "115933905-YFWzzwgHETkcEf3rJ4xDHlyUf3pn3d9c6ppedw4J",
            "access_token_secret": "Z6QmNerdsxwbtBJJknYyeglA3XGhyhJVClvXpgCMlQYau"
        }

        string = str(binascii.hexlify(os.urandom(20)))
        list = [
            'Total signatures till now is ',
            'The latest result of the petition is ',
            'Till now the number of collected signatures is '
        ]
        ran = random.choice(list)
        message = string + ' Ignore this. \n' + ran + str(self.get_data())

        #posting to twitter
        api = self.get_api(cfg)
        api.update_status(status=ran+str(self.get_data()))
        self.stdout.write('posted to twitter')


        #posting to facebook
        #graph = facebook.GraphAPI('EAACEdEose0cBAPy1IlZAeKlqNZAMiv8O9diMe0GCEP6vZBdZBdWCR6yfFbVzqQKPxQY8iKviafRNCfFlWXvMSSoWHfqi0uoGn0rtYEJKuOU0LIbAuJTXgVmmsCZAsZCj1ttlNVIs8hP9SJuC6UM1ZALrJcmDPoObZA6aoZCvHvN5I8cZC313R3oPabGVW2dXTjkZBzj3wejiZClvpgZDZD')
        graph = facebook.GraphAPI(user.extra_data['access_token'])
        graph.put_object("me", "feed", message=message)


        self.stdout.write('posted to facebook')
