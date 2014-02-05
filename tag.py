
import json
import urllib
import urllib2
import re
import sys 

## tag by dbpedia spotlight service; instead of only use 'actor','movie','show' as tags, I use all instances identified.
def tag(jsonfile):
	support = "0"
	confidence = "0"
	spotter = "AtLeastOneNounSelector"
	##sparql = ""
	##types = "DBpedia:Person,DBpedia:TelevisionShow,DBpedia:Film"
	types = ""
	spotlight = "http://spotlight.dbpedia.org/rest/annotate"

	with open(jsonfile) as json_file:
		json_data = json.load(json_file)


	for video in json_data:
		text = video['description'] + ' ' + video['title']		
		try:
			args = urllib.urlencode([("disambiguator","Document"),("support",support),("confidence",confidence),#("types",types),
("text",text)])
		except UnicodeError:
			pass
		request = urllib2.Request(spotlight, data=args, headers={"Accept":"application/json"})
		try:
			answer = urllib2.urlopen(request).read()
			tags = re.findall('"@surfaceForm": "(.*?)",',answer)
			tags = [tag.lower() for tag in tags if tag!="http://"]
			if not tags : video["tag"] = video["title"].split()
			tags = list(set(tags))
			video["tags"] = tags
		except urllib2.HTTPError:
			print "404"
		except urllib2.URLError:
			print "Timeout"	
	with open("DataWithTag.json",'w') as outfile:
		json.dump(json_data,outfile)
				

def main():
	if len(sys.argv) >= 2:
		jsonfile = sys.argv[1]
	else : jsonfile = "CodeAssignmentDataSet.json"
	tag(jsonfile)

if __name__ == '__main__':
	main()
