import urllib2		
import json
#import os

word = raw_input("Enter word to search ")
print("Word: "+ word)

url = 'http://glosbe.com/gapi/translate?from=eng&dest=eng&format=json&phrase=' + word + '&pretty=true'
#url stores the json formatted output from Glosbe


result = json.load(urllib2.urlopen(url))	#json representation of url

print("Meanings: ")
i = 1
for mean in result['tuc'][0]['meanings']:
	print(str(i) + ". " + mean['text'] + "\n")
	i += 1


