#  Flask app to run the web app
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import os
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

app.config["ALLOWED_EXTENSIONS"] = set(
	["midi"]
)


def allowed_file(filename):
	return (
		"." in filename
		and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
	)

@app.route('/success', methods=['POST'])
def success():
	if request.method == 'POST':
		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			return redirect(request.url)
		if file and allowed_file(file.filename):
			f= request.files['file']
			f.save(os.path.join(f.filename))
			return render_template('success.html', audio_path=f.filename)

if __name__ == '__main__':
	app.run(debug=True)
