import xml.etree.ElementTree as ET
import csv
from datetime import datetime

tree = ET.parse('NUK.xml')
root = tree.getroot()

print(root.tag)

with open('NUK.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')

    i = 0
    for x in root.findall('Station'):
        val = float(x.find('Value').text)
        lat = float(x.find('Latitude').text)
        lon = float(x.find('Longitude').text)
        date = x.find('Date').text
        date = date.replace('T', ' ')
        date = date.replace('Z', '')
        dt_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

        day = dt_obj.dayž
        month = dt_obj.month
        year = dt_obj.year

        writer.writerow([i, val, lat, lon, day, month, year])
        print(i)
        print(val)
        print(lat)
        print(lon)
        print(date)
        print(dt_obj)
        i = i + 1

