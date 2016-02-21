from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from collegeinfo import Colleges
from analyzer import Analyzer

app = Flask(__name__)
c = Colleges()
a = Analyzer()

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
	school = request.form["school"].encode('utf-8')
	coords = c.get_coords_from_name(school)
	yakList = a.get_yaks_by_coords(coords[0],coords[1])
	ave = a.get_weighted_average_sentiments(yakList)

	print "__________________"
	print ave
	print "__________________"

	r = ''
	for i in yakList:
		r += (i.message+'\n')
		
	return r


if __name__ == "__main__":
	app.run(debug=True)
