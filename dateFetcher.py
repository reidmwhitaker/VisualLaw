import os
import json
import codecs
from datetime import datetime
import csv

dates = {}
dir = "/Volumes/WD My Passport/LILProject/References_Curated"
for file in os.listdir(dir):
    if file.endswith(".json"):
        json_data = open(dir + "/" + file).read()
        #print(file)
        data = json.loads(json_data)
        count = data["citation_count"]
        date = data["date"][0:4]
        if date.isdigit():
            try:
                dates[date] = dates[date] + count
            except:
                dates[date] = count
with open('ReferenceYears.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for date, count in dates.items():
       writer.writerow([date, count])
