from codecs import open

t = open("reproducing-autonomy.html", "r", "utf-8").read()

t = t.replace('<p>by Kerstin Stakemeier &amp; Marina Vishmidt</p>','<p class="author" property="http://purl.org/dc/terms/creator">by Kerstin Stakemeier &amp; Marina Vishmidt</p>')

o = open("reproducing-autonomy.html", "w", "utf-8")
o.write(t)
