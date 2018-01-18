from urllib.request import urlopen
import json

def get_jsonparsed_data(url):

    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


url = ("http://maps.googleapis.com/maps/api/geocode/json?"
       "address=googleplex&sensor=false")
print(get_jsonparsed_data(url))