import csv
import requests
import json
from IPython import embed

places = 'places.csv'
url = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyDC8ORRittWncpAu7M6L5_9SWsd-aGeeXk"
headers = {
    'cache-control': "no-cache",
    'postman-token': "d33b1c90-dffd-7491-f9ed-51e7a004f040"
    }

file=open( places, "r")

reader = csv.reader(file)
places = []

for line in reader:
    place=line[0]+" "+line[1]+" "+line[2]+" "+line[3]
    place= place.replace(" ","+")
    places.append(place)

latLongs = []
for place in places:
    querystring = {"address":place}
    response = requests.request("GET", url, headers=headers, params=querystring)
    location = json.loads(response.text)["results"][0]["geometry"]["location"]
    latLongs.append(location)

jsonLocations = json.dumps(latLongs)


with open("places.json", "w") as text_file:
    text_file.write(jsonLocations)
