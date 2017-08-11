import os
import json
import codecs

titles = ""
titlesWeighted = ""
dir = "/Volumes/WD My Passport/LILProject/References_Curated"
for file in os.listdir(dir):
    if file.endswith(".json"):
        json_data = open(dir + "/" + file).read()
        #print(file)
        data = json.loads(json_data)
        count = data["citation_count"]
        titles = titles + ", " + data["title"]
        for i in range(0,count):    
	        titlesWeighted = titlesWeighted + ", " + data["title"]

text_file = codecs.open("TitlesWeighted.txt", "w", encoding="utf-8")
text_file.write(titlesWeighted)
text_file.close()
text_file = codecs.open("Titles.txt", "w", encoding="utf-8")
text_file.write(titles)
text_file.close()
