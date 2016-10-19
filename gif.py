from flask import Flask, render_template, request
import giphypop
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import urllib,json

app = Flask(__name__)

# API Key from Giphy
g = giphypop.Giphy()

# HTML Pages
@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/results')
def results():
	# do search
	gifmedia = [] # Make empty list
	gifurl = []
	gifs = request.values.get("keyword") # You should define search key word as 'keyword' on html file.
	results = g.search(gifs) # Search gifs and put it into results 

	for result in results:
		gifmedia.append(result.media_url)
		gifurl.append(results.url)


	return render_template('results.html', media=gifmedia, url=gifurl)
 
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':

	port = int(os.environ.get("PORT", 5000)) # These next 2 lines are needed for Heroku 
	app.run(host="0.0.0.0", port=port)

