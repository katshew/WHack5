from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)

GoogleMaps(app)

@app.route('/')
def index(): 
	mymap = Map(
		identifier="view-side", 
		lat=37.4419, 
		lng=-122.1419, 
		markers=[(37.4419, -122.1419)]
	)
	
	return render_template('index.html', mymap=mymap)

@app.route('/searchSchool', methods=['POST']) 
def testing(): 
	return render_template('test.html', school=request.form['school'])

if __name__ == "__main__": 
	app.run(debug=True)



