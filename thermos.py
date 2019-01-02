from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():

	return render_template('index.html', title="Title passed from the view to the template", text= ["first", "second", "third"])

if __name__ == '__main__':
	app.run(debug=True)