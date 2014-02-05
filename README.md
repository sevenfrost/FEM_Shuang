FEM
===

video recommendation based on content similarity

<p>Without considering how to handle scaling and incremental incoming files, use a straightforward way to tag the videos and compute video similarity.
</p>

<p>Two python files provided. One for tagging, one for recommendation.
<ul>
<li>"tag.py". Identify important entities from description and summary of videos by using DBpedia Spotlight web service. Instead of only tag by actor, film, and show names, I use all entities identified to tag each video. Taged file "DataWithTag.json" is the original data set with tags for each video.</li>
<li>"VideoRecommend.py". Use jaccard distance as similarity measure between videos, did not put weight on actors, films and shows. <li>
</ul>

<p>To programs are seperated. Since I provided the tag file, to get the recommended video, you can simply :
python VideoRecommend.py
</p>
<p>To assign tags : 
python tag.py.
This might take 1 or two minutes, since it uses the web service.
</p>
