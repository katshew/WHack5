from flask import Flask, render_template, request, jsonify
from collegeinfo import Colleges
from analyzer import Analyzer

app = Flask(__name__)
c = Colleges()
a = Analyzer()

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

@app.route('/getWeightedAverages', methods=['POST'])
def weighted():
    return jsonify(a.get_weighted_average_sentiments())

@app.route('/getKeywords', methods=['POST'])
def keywords():
    # return jsonify({"keywords":a.get_keywords_for_yaks()})
    return str(a.get_keywords_for_yaks())

if __name__ == "__main__":
	app.run(debug=True)
