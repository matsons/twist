from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def main():
	return "Welcome to TwisT"
	# sexy social splash screen

@app.route("/user/<username>")
def show_user_profile(username):
	# Show profile and last 10 posts?
	return "Hey here's the page for {}".format(username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
	# return templated post from id
	# pull post info from db
	return "Hey here's the post {}".format(post_id)

with app.test_request_context():
	print(url_for('main'))
	print(url_for('show_user_profile', username='smatson'))
if __name__=="__main__":
	app.run() 
