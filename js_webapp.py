from flask import Flask, request, render_template, json, make_response
import jinja2

from api import Api


app = Flask(__name__)

# The "secret key" is needed for the Flask session machinery. In a real
# application, this should be a unguessable string and should NOT be
# checked into version control. Typically, one stores this as an
# environmental variable outside of the Flask app and gets it with
# os.environ['MY_SECRET_KEY']. For our exercise purposes, though, it's
# fine to have this here.
app.secret_key = 'look at that sweet key!'

# Make it an error to use undefined variables in templates.
# (This isn't required for this exercise, but is a good practice for Flask/Jinja2;
# otherwise errors are silently ignored, which makes for harder debugging.)
app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def index():
    html = render_template("wall.html")
    return html


# We're routing this next function to two different routes:
#
#   - /api/wall, but if you use this, we'll set the action to ="get"
#   - /api/wall/<action>, where we get the action from the URL
#
# Since we only want GET requests used for our GET method, and POST
# requests used for our set method, we check that inside the code.

@app.route("/api/wall", defaults={"action": "get"}, methods=['GET'])
@app.route("/api/wall/<action>", methods=['GET', 'POST'])
def wall_action(action):
    api = Api()

    if action == "get" and request.method == 'GET':
        result = api.get()

    elif action == "set" and request.method == 'POST':
        # Get the message from the "m" argument passed in the POST.
        # (to get things from a GET response, we've used request.args.get();
        # this is the equivalent for getting things from a POST response)
        msg = request.form.get('m').strip()

        # Check to make sure the message is being sent to the API
        if msg is None:
            result = api.error("You did not specify a message to set.")
        elif msg == "":
            result = api.error("Your message is empty")
        else:
            result = api.set(msg)
    else:
        result = api.error("You did not specify a valid request method.")

    # In order for us to return a response that isn't just HTML, we turn our
    # response dictionary into a string-representation (using json.dumps),
    # then use the flask `make_response` function to create a response object
    # out of this.
    response = make_response(json.dumps(result))

    # We can then set some headers on this response object:

    # Access-Control-Allow-Origin isn't needed for this example, but it's
    # a demonstration of a useful feature: since it should be safe to allow
    # Javascript from websites other than ours to get/post to our API, we
    # explicitly allow this.
    response.headers['Access-Control-Allow-Origin'] = "*"

    # Setting the MIMETYPE to JSON's will explicitly mark this as JSON;
    # this can help some client applications understand what they get back.
    response.mimetype = "application/json"

    return response


if __name__ == "__main__":
    app.run(debug=True)