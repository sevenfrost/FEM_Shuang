
import json
from numpy import *

## use Jaccard distance as distance measure.
def jaccard_sim(l1,l2):
	l1 = set(l1)
	l2 = set(l2)
	if l1 or l2 :
		return len(l1.intersection(l2))/float(len(l1.union(l2)))
	else : return 0


def rec():
	with open("DataWithTag.json") as json_file:
		json_data = json.load(json_file)
	sims = zeros((len(json_data),len(json_data)))
	i = 0
	video_index = []
	index = 0
	for video in json_data:
		video_index.append(video["title"])
		index += 1
	
	for video in json_data:
		j = 0
		for video_com in json_data:
			if j > i : sims[i][j] = jaccard_sim(video["tags"],video_com["tags"])
			else : sims[i][j] = sims[j][i]
	 		j += 1
		i += 1
	f = open("RecommendedVideo.json","w")
	f.write("[")
	for i in range(len(json_data)):
		sort_index = sims[i].argsort(kind = "quicksort")[::-1]
		recs = [video_index[sort_index[0]],video_index[sort_index[1]],video_index[sort_index[2]]]
		newData = json.dumps({"title":video_index[i],"recommended video":recs},sort_keys=True, indent = 4)
		f.write(newData)
		f.write(",\n")
	f.write("]")

if __name__ == '__main__':
	rec()
