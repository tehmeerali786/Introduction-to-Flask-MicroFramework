from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash

from forms import BookmarkForm




app = Flask(__name__)

bookmarks = []


app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'

class User:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	def initials(self):
		return "{}. {}.".format(self.firstname[0], self.lastname[0])


def store_bookmark(url):

	bookmarks.append(dict(

		url = url,
		user = 'Tehmeer Ali Paryani',
		date = datetime.utcnow()

		))



def new_bookmarks(num):
	return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


bookmarks = []
		


@app.route('/')
@app.route('/index')
def index():

	return render_template('index.html', new_bookmarks=new_bookmarks(5))

@app.route('/add', methods=['GET', 'POST'])
def add():
	form = BookmarkForm()
	if form.validate_on_submit():
		url = form.url.data
		description = form.description.data
		store_bookmark(url)
		flash("Stored bookmarks '{}'".format(url))
		return redirect(url_for('index'))
	return render_template('add.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	app.run(debug=True)