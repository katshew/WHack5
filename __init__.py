from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index(): 
	return render_template('index.html')

@app.route('/searchSchool', methods=['POST']) 
def testing(): 
	return render_template('test.html', school=request.form['school'])

if __name__ == "__main__": 
	app.run(debug=True)

