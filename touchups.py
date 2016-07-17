# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from codecs import open

t = open("reproducing-autonomy.html", "r", "utf-8").read()

t = t.replace('<p>by Kerstin Stakemeier &amp; Marina Vishmidt</p>','<p class="Chapter_Authors" property="http://purl.org/dc/terms/creator">by Kerstin Stakemeier &amp; Marina Vishmidt</p>')

t = t.replace('<p><img src="media/image1.png" width="121" height="121" /></p>', '<p class="centered"><img src="Images/M.svg" width="60" height="60" /></p>')
t = t.replace('<p><img src="media/image2.png" width="78" height="24" /></p>', '<p class="centered"><img src="Images/Mute-logo2.png" width="78" height="24" /></p>')

t = t.replace('<p>Mute Books, LondonMUTE LOGO</p>','<div class="white">&nbsp;</div>\n<p><img width="123" height="39" src="Images/Mute-logo2.png"/></p>')

t = t.replace('<div class="footnotes">', '<h1>Footnotes</h1>\n<div class="footnotes">')

t = t.replace("""<ol style="list-style-type: decimal">
<li><p>The exclusive concentration of artistic talent in individuals and the suppression of it in the greater masses is the result of the division of labour.</p></li>
</ol>
<p>– Karl Marx and Friedrich Engels, <em>The German Ideology</em> (1846)</p>
<ol style="list-style-type: decimal">
<li><p>As no autonomy of art is conceivable without the concealing of labour, this becomes, within high capitalism, by means of the antagonisms growing from such dominance, problematic and programmatic […] The artwork substantiates what ideology otherwise denies: labour desecrates.</p></li>
</ol>
<p>– Theodor W. Adorno, <em>In Search of Wagner</em> (1952)</p>
<ol style="list-style-type: decimal">
<li><p>What is theoretically right can be politically wrong. Theory is understanding and foresight, knowledge, that is, be it only one-sided, of the objective tendency and process. Politics on the contrary is the will to revolutionize this process, an all-encompassing rejection of its objectivity, subjective action, so that this objectivity cannot assert itself and does not carry off the victory. Theory is anticipation. Politics is intervening.</p></li>
</ol>
<p>– Mario Tronti, <em>Workers and Capital</em> (1962)</p>
<ol style="list-style-type: decimal">
<li><p>As visual art, a highly conceptual work still stands or falls by what it looks like, but the primary, rejective trends in their emphasis on singleness and autonomy have limited the amount of information given, and therefore the amount of formal analysis possible.</p></li>
</ol>
<p>– Lucy R. Lippard and John Chandler, <em>The Dematerialization of Art</em> (1967)</p>
<ol style="list-style-type: decimal">
<li><p>The work of art leaves the domain of representation to become ‘experience’, transcendental empiricism or science of the sensible.</p></li>
</ol>
<p>– Gilles Deleuze, <em>Difference and Repetition</em> (1968)</p>
<ol style="list-style-type: decimal">
<li><p>Efforts are made to avoid everything which could contribute to the articulation of this conflict between aspiration and reality […] this articulation is avoided in a simple way […] in that a certain part of life is severed from the societal one, is tabooed, in giving it the name private life […] this tabooing entails that the specific exploitive relationship under which women are kept is suppress(ed.)</p></li>
</ol>
<p>– Helke Sander, Action Council for the Liberation of Women speech at the SDS Conference (1968)</p>
<ol style="list-style-type: decimal">
<li><p>No theory can develop without eventually encountering a wall, and practice is necessary for piercing this wall […] Representation no longer exists; there’s only action – theoretical action and practical action which serve as relays and form networks.</p></li>
</ol>
<p>– Gilles Deleuze, ‘Intellectuals and Power: A Discussion between Michel Foucault and Gilles Deleuze’ (1972)</p>
<ol style="list-style-type: decimal">
<li><p>The return to the immanence of the work in art [entails] the rigid separation of forming and acting […] the end-result is the amputation of culture from its dimension of praxis […] the obsessive fear of the artist without a work proves to be the heritage of the bourgeois fission of one and the same artistic process of production into art and life.</p></li>
</ol>
<p>– Peter Gorsen, <em>Transformierte Alltäglichkeit oder Transzendenz der Kunst</em> (1974)</p>
<ol style="list-style-type: decimal">
<li><p>A theory of socialization (is needed) […] which understands Freudian ‘individuation’ as a working process and associates the artistic working process with it, comparing it […] early childhood socialization [is characterized by] the confrontation of the interfamiliar ‘sphere of reproduction’ with the later ‘sphere of profession’ […] this separation of the sphere of production and that of reproduction relies on the identification of production-labour-profession, the sphere of production <em>posited</em> by society.</p></li>
</ol>
<p>– Gisela Dischner, <em>Sozialisationstheorie und materialistische Ästhetik</em> (1974)</p>
<ol style="list-style-type: decimal">
<li><p>One of the questions we have yet to answer is whether women do want the same things that men have wanted; whether ‘greatness’ in its present form is in fact desirable.</p></li>
</ol>
<p>– Lucy R. Lippard, ‘Changing Since Changing’ (1976)</p>
<ol style="list-style-type: decimal">
<li><p>What defines labor as such is not the production of a commodity or even a ‘useful effect’ […] but rather the production of value that is appropriated by another as profit. What our modern myths of artistic production have effaced is […] that the professional artist, like other laborers, works not only for his or her satisfaction, but for the enrichment of others.</p></li>
</ol>
<p>– Andrea Fraser, ‘Creativity = Capital?’ (1986)</p>
<ol style="list-style-type: decimal">
<li><p>The depicted [<em>dargestellte</em>] structure of capital is idealistic, its depiction [<em>Darstellung</em>] is not. Capital is depicted after the model of an absolute subject, the subject of theory in its dependency on the given material proves to be a not-absolute, historical subject.</p></li>
</ol>
<p>– Frank Kuhne, <em>Begriff und Zitat bei Marx</em> (1995)</p>
<ol style="list-style-type: decimal">
<li><p>The submission of dependent labour can no longer be only formal, that means it can no longer take only the form of a separation of the labour force from its personalized bearer, but it must become real, the dependency of labour needs to be restored in its subjective character, in its singularity. It is the living labour as living, which needs to be subjugat(ed.)</p></li>
</ol>
<p>– Yann Moulier Boutang, preface to <em>Umherschweifende Produzenten</em> (1998)</p>
<ol style="list-style-type: decimal">
<li><p>We frame the character’s conceptual focal points. We might interpret a car commercial as a hairdo, an ideology as a designer skirt tone, a banking situation as a cheekbone, copyright issues as a jaw line, or maybe an application as facial agenda […] It is the value of how things break down now.</p></li>
</ol>
<p>– Ryan Trecartin, ‘Ryan Trecartin in Conversation with Cindy Sherman’ (2011)</p>
<ol style="list-style-type: decimal">
<li><p>‘We called ourselves Chia Jen, or The Family’, the choreographer Simone Forti wrote of the collective she lived in during the late 1960s. ‘The life we lived in common provided a matrix for the profuse visions we lived out in various twilights’ […] Using Contemporary Art’s self-reflexivity, it could be that anti-brands like American Apparel, achieving much of their psychic power from the real-time lives of their employees, are able to reach more deeply into the culture than art ever can.</p></li>
</ol>
<p>– Chris Kraus, <em>Where Art Belongs</em> (2011)</p>
<ol style="list-style-type: decimal">
<li><p>The usual effort to locate and identify the self, at once shifts into considerations about its deployment […] The outcome is open, if one understands this deployment of oneself not only as competing for attention but as a critical gesture or revelation.</p></li>
</ol>
<p>– Karolin Meunier, <em>Return to Inquiry</em> (2012)</p>
<ol style="list-style-type: decimal">
<li><p>The phenomena of self-positioning, self-affection, self-referentiality as opening towards processuality, creation of possibilities, and initiation of becoming and mutation are originary. But these autopoietic spaces only gain materiality by transversalizing, repositioning and reconfiguring all realms considered as ‘structural’ (economic, political, social, linguistic, sexual, scientific, etc.)</p></li>
</ol>
<p>– Maurizio Lazzarato, lecture given at Psychopathologies of Cognitive Capitalism, Berlin (2013)</p>""", """<ol style="list-style-type: decimal">
<li><p>The exclusive concentration of artistic talent in individuals and the suppression of it in the greater masses is the result of the division of labour.</p>
<p>– Karl Marx and Friedrich Engels, <em>The German Ideology</em> (1846)</p></li>
<li><p>As no autonomy of art is conceivable without the concealing of labour, this becomes, within high capitalism, by means of the antagonisms growing from such dominance, problematic and programmatic […] The artwork substantiates what ideology otherwise denies: labour desecrates.</p>
<p>– Theodor W. Adorno, <em>In Search of Wagner</em> (1952)</p></li>
<li><p>What is theoretically right can be politically wrong. Theory is understanding and foresight, knowledge, that is, be it only one-sided, of the objective tendency and process. Politics on the contrary is the will to revolutionize this process, an all-encompassing rejection of its objectivity, subjective action, so that this objectivity cannot assert itself and does not carry off the victory. Theory is anticipation. Politics is intervening.</p>
<p>– Mario Tronti, <em>Workers and Capital</em> (1962)</p></li>
<li><p>As visual art, a highly conceptual work still stands or falls by what it looks like, but the primary, rejective trends in their emphasis on singleness and autonomy have limited the amount of information given, and therefore the amount of formal analysis possible.</p>
<p>– Lucy R. Lippard and John Chandler, <em>The Dematerialization of Art</em> (1967)</p></li>
<li><p>The work of art leaves the domain of representation to become ‘experience’, transcendental empiricism or science of the sensible.</p>
<p>– Gilles Deleuze, <em>Difference and Repetition</em> (1968)</p></li>
<li><p>Efforts are made to avoid everything which could contribute to the articulation of this conflict between aspiration and reality […] this articulation is avoided in a simple way […] in that a certain part of life is severed from the societal one, is tabooed, in giving it the name private life […] this tabooing entails that the specific exploitive relationship under which women are kept is suppress(ed.)</p>
<p>– Helke Sander, Action Council for the Liberation of Women speech at the SDS Conference (1968)</p></li>
<li><p>No theory can develop without eventually encountering a wall, and practice is necessary for piercing this wall […] Representation no longer exists; there’s only action – theoretical action and practical action which serve as relays and form networks.</p>
<p>– Gilles Deleuze, ‘Intellectuals and Power: A Discussion between Michel Foucault and Gilles Deleuze’ (1972)</p></li>
<li><p>The return to the immanence of the work in art [entails] the rigid separation of forming and acting […] the end-result is the amputation of culture from its dimension of praxis […] the obsessive fear of the artist without a work proves to be the heritage of the bourgeois fission of one and the same artistic process of production into art and life.</p>
<p>– Peter Gorsen, <em>Transformierte Alltäglichkeit oder Transzendenz der Kunst</em> (1974)</p></li>
<li><p>A theory of socialization (is needed) […] which understands Freudian ‘individuation’ as a working process and associates the artistic working process with it, comparing it […] early childhood socialization [is characterized by] the confrontation of the interfamiliar ‘sphere of reproduction’ with the later ‘sphere of profession’ […] this separation of the sphere of production and that of reproduction relies on the identification of production-labour-profession, the sphere of production <em>posited</em> by society.</p>
<p>– Gisela Dischner, <em>Sozialisationstheorie und materialistische Ästhetik</em> (1974)</p></li>
<li><p>One of the questions we have yet to answer is whether women do want the same things that men have wanted; whether ‘greatness’ in its present form is in fact desirable.</p>
<p>– Lucy R. Lippard, ‘Changing Since Changing’ (1976)</p></li>
<li><p>What defines labor as such is not the production of a commodity or even a ‘useful effect’ […] but rather the production of value that is appropriated by another as profit. What our modern myths of artistic production have effaced is […] that the professional artist, like other laborers, works not only for his or her satisfaction, but for the enrichment of others.</p>
<p>– Andrea Fraser, ‘Creativity = Capital?’ (1986)</p></li>
<li><p>The depicted [<em>dargestellte</em>] structure of capital is idealistic, its depiction [<em>Darstellung</em>] is not. Capital is depicted after the model of an absolute subject, the subject of theory in its dependency on the given material proves to be a not-absolute, historical subject.</p>
<p>– Frank Kuhne, <em>Begriff und Zitat bei Marx</em> (1995)</p></li>
<li><p>The submission of dependent labour can no longer be only formal, that means it can no longer take only the form of a separation of the labour force from its personalized bearer, but it must become real, the dependency of labour needs to be restored in its subjective character, in its singularity. It is the living labour as living, which needs to be subjugat(ed.)</p>
<p>– Yann Moulier Boutang, preface to <em>Umherschweifende Produzenten</em> (1998)</p></li>
<li><p>We frame the character’s conceptual focal points. We might interpret a car commercial as a hairdo, an ideology as a designer skirt tone, a banking situation as a cheekbone, copyright issues as a jaw line, or maybe an application as facial agenda […] It is the value of how things break down now.</p>
<p>– Ryan Trecartin, ‘Ryan Trecartin in Conversation with Cindy Sherman’ (2011)</p></li>
<li><p>‘We called ourselves Chia Jen, or The Family’, the choreographer Simone Forti wrote of the collective she lived in during the late 1960s. ‘The life we lived in common provided a matrix for the profuse visions we lived out in various twilights’ […] Using Contemporary Art’s self-reflexivity, it could be that anti-brands like American Apparel, achieving much of their psychic power from the real-time lives of their employees, are able to reach more deeply into the culture than art ever can.</p>
<p>– Chris Kraus, <em>Where Art Belongs</em> (2011)</p></li>
<li><p>The usual effort to locate and identify the self, at once shifts into considerations about its deployment […] The outcome is open, if one understands this deployment of oneself not only as competing for attention but as a critical gesture or revelation.</p>
<p>– Karolin Meunier, <em>Return to Inquiry</em> (2012)</p></li>
<li><p>The phenomena of self-positioning, self-affection, self-referentiality as opening towards processuality, creation of possibilities, and initiation of becoming and mutation are originary. But these autopoietic spaces only gain materiality by transversalizing, repositioning and reconfiguring all realms considered as ‘structural’ (economic, political, social, linguistic, sexual, scientific, etc.)</p>
<p>– Maurizio Lazzarato, lecture given at Psychopathologies of Cognitive Capitalism, Berlin (2013)</p></li>""")

o = open("reproducing-autonomy.html", "w", "utf-8")
o.write(t)
