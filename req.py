import requests
import json

URL_ALL = "https://remap.jrc.ec.europa.eu/api/stations?type=Last&startDate=20230516000000&endDate=202305230"

URL = "https://remap.jrc.ec.europa.eu/api/stations"


PARAMS = {'type':'Last', 'startDate':'20230418000000', 'endDate':'20230523074713'}

r = requests.get(url=URL, params=PARAMS)


data = r.json()
#json_dat = json.loads(data[0])
#print(json_dat)

for d in data:
    print(len(d['code']))
    print(d['code'])
    print(d['country'])

