from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello, FatCloud!'

@app.route('/game_1')
def game_1():
	return render_template('game_1.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'nothing here!', 404
