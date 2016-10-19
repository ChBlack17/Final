from flask import Flask, render_template, request
import os
import giphypop
app = Flask(__name__)

# HTML Pages:

# Index
@app.route('/')
def index():
	return render_template('index.html') 

# About
@app.route('/about')
def about():
    return render_template('about.html')

#Results (Search from Giphy)
@app.route('/results')
def results():
	searchterm = request.values.get('name') 
	giphyobject = giphypop.Giphy()
	results = giphyobject.search(searchterm)
	return render_template('results.html', results=results)	 

# These next lines are needed for Heroku:
if __name__ == '__main__':

	port = int(os.environ.get("PORT", 5000))  
	app.run(host="0.0.0.0", port=port)
