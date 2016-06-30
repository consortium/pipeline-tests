from __future__ import unicode_literals

from codecs import open

t = open("reproducing-autonomy.html", "r", "utf-8").read()

t = t.replace('<p>by Kerstin Stakemeier &amp; Marina Vishmidt</p>','<p class="author" property="http://purl.org/dc/terms/creator">by Kerstin Stakemeier &amp; Marina Vishmidt</p>')

t = t.replace('<p>Mute Books, LondonMUTE LOGO</p>','<div class="white">&nbsp;</div>\n<p><img width="123" height="39" src="Images/Mute-logo2.png"/></p>')

t = t.replace('<div class="footnotes">', '<h1>Footnotes</h1>\n<div class="footnotes">')

o = open("reproducing-autonomy.html", "w", "utf-8")
o.write(t)
