import os
from flask import Flask, url_for
# app = Flask(__name__)

def create_app(test_config=None):
	"""Create and config Twist"""
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='key',
		# db in whatever folder this is lanched FROM
		DATABASE=os.path.join(app.instance_path, 'twist.sqlite')
	)

	if test_config is None:
		# load instance config when not testing
		app.config.from_pyfile('config.py', silent=True)
	else:
		# load test config
		app.config.update(test_config)

	# confirm instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	@app.route('/hello/<name>')
	def hello(name):
		return 'Hello, {}'.format(name)

	from twist import twist
	# with app.test_request_context():
		# print(url_for('main'))
		# print(url_for('show_user_profile', username='smatson'))
	return app

