# Author:      Marco Squarcina <lavish@gmail.com>
# License:     MIT, see LICENSE for details

import datetime

author = "Luca Postregna"
path_separator = "/"
prefix = "/"
home = "/"
src_ext = {"textile": "textile"}
dst_ext = "html"
hidden = set(["404.textile", "500.textile", "privacy.textile"])
current_time = datetime.datetime.now()

def header(node):
	"""Builds the header and returns it to a string."""
	return '''<!DOCTYPE html>
	<html lang="''' + language + '''">
	<head>
		<title>''' + title + ' | ' + node.name + '''</title>
		<meta name="author" content="''' + author + '''" />
		<meta name="keywords" content="''' + keywords + '''" />
		<meta name="description" content="''' + description + '''" />
		<meta content="text/html; charset=UTF-8" http-equiv="content-type" />
		<link rel="shortcut icon" href="/images/bassanese.ico" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" /> 
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
		<script type="text/javascript" src="/js/hashgrid.js"></script>  
		<script type="text/javascript" src="/js/flux.min.js"></script>  
		<script type="text/javascript" src="/js/slider.js"></script>  
		<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
		<script type="text/javascript" src="http://widgets.twimg.com/j/2/widget.js"></script>
		<script type="text/javascript" src="/js/googleanalytics.js"></script>  
	</head>
	<body>
		<header class="container_16">
			<div id="title" class="grid_9">
				<a href="/" title="home page">
					<h1>''' + site_name + '''</h1>
	<!--				<h1>''' + subname + '''</h1> -->
				</a>
				<h2>''' + site_desc2 + '''</h2>
				<h2>''' + site_desc1 + '''</h2>
        <!--				<div id="buttons">
					<div id="tripadvisor" class="alpha grid_2">
						<a href="#" title="Agriturismo Mauro su TripAdvisor">
							<p class="hide">tripadvisor</p>
						</a>
					</div> 
					<div id="facebook" class="omega grid_1">
						<a href="https://www.facebook.com/AgriturismoMauroVini" title="Agriturismo Mauro su Facebook">
							<p class="hide">facebook</p>
						</a>
					</div>
				</div> -->
			</div>
			<div id="hright" class="grid_7 clearfix">
				<div id="contacts">
					di Roberto Mauro e Dolores Pascolo<br/><br/>
					<a title="Agriturismo Mauro su Google Maps" href="">Via Vittorio Veneto 1, Fraz. Oleis<br/>Manzano, 33044 Udine</a><br/><br/>
					tel: +39 3803516322, +39 0432740029<br/>
				     	mail: <a href="#" title="indirizzo email dell'agriturismo mauro">info@agriturismomauro.it</a>
				</div>
			</div>
			<div class="clear"></div>
		</header>
		<div id=center>
			<div class="container_16">
'''
def footer(node):
	"""Builds the footer and returns it to a string."""
	return '''
			</div>
		</div><!-- chiuso center -->
		<div class="container_16">
			<footer class="grid_16 clearfix">
				&copy; ''' + str(current_time.year) + ''' <a title="Il blog di Luca Postregna" href="http://luca.postregna.name">Luca Postregna</a> ::
				<a title="La licenza Creative Commons" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">license</a> ::
				<a title="Privacy" href="/privacy.html">privacy</a> ::
				<a title="xhtml validator" href="http://validator.w3.org/check?uri=referer">xhtml</a> <a title="css validator" href="http://jigsaw.w3.org/css-validator/check/referer">css</a> ::
				update: ''' + str(current_time.strftime("%Y%m%d")) + '''
			</footer>
			<div class="clear"></div>
		</div>
	</body>
</html>'''
