from flask import Flask, request, session, render_template, g, redirect, url_for, flash, json, Response, make_response
from api import Api
import jinja2

app = Flask(__name__)
app.secret_key = 'look at that sweet key!'
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index():
	html = render_template("wall.html")
	return html

@app.route("/api/wall", defaults={"action":"get"}, methods=['GET'])
@app.route("/api/wall/<action>", methods=['GET', 'POST'])
def api(action):
	api = Api()

	if action == "get" and request.method == 'GET':
		response = api.get()
	elif action == "set" and request.method == 'POST':
		# Get the message from the "m" argument passed in the address bar.
		msg = request.form.get('m', None)

		# Check to make sure the message is being sent to the API
		if msg == None:
			response = api.error("You did not specify a message to set.")
		elif msg == "":
			response = api.error("Your message is empty")
		else:
			response = api.set(msg)
	else:
		response = api.error("You did not specify a valid request method.")

	response = make_response(json.dumps(response))
	response.headers['Access-Control-Allow-Origin'] = "*"
	response.mimetype = "application/json"
	return response

if __name__ == "__main__":
	app.run(debug=True)