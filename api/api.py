import flask
from flask import request, jsonify
import app as ap

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/api/v1/resources/func/setValues", methods=["GET"])
def setValues():
    if 'rownum' in request.args and 'name' in request.args:     
        ap.setAllValues(request.args['rownum'], request.args['name'])
    else: 
        return "Error: No rownum(Row Number) and name specified"

app.run()


