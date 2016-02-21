from flask import Flask, render_template, request, jsonify
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
	return render_template('index.html')

@app.route('/searchSchool', methods=['POST'])
def search():
	school = request.form["school"].encode('utf-8')
	coords = c.get_coords_from_name(school)
	yakList = a.get_yaks_by_coords(coords[0],coords[1])
	#ave = a.get_weighted_average_sentiments(yakList)
	#keywords = a.get_keywords_for_yaks(yakList)
	yaks = []
	for i in range(len(yakList)):
		yaks.append({"yak":yakList[i].message, "votes":yakList[i].likes})

	gps = [{"lat":coords[0], "long":coords[1]}]

	return jsonify({"yaks":yaks, 'coords':gps})


if __name__ == "__main__":
	app.run(debug=True)
