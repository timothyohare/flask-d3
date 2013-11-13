"""
This file is part of the flask+d3 Hello World project.
"""
import json
import flask
from flask import request
import numpy as np
import csv


app = flask.Flask(__name__)


@app.route("/hello")
def index():
    """
    When you request the root path, you'll get the index.html template.

    """
    return flask.render_template("index.html")


@app.route("/")
def gindex():
    """
    When you request the gaus path, you'll get the gaus.html template.

    """
    mux = request.args.get('mux', '')
    muy = request.args.get('muy', '')
    if len(mux)==0: mux="3."
    if len(muy)==0: muy="3."
    #return flask.render_template("gaus.html",mux=mux,muy=muy)
    return flask.render_template("holes.html")


@app.route("/data")
@app.route("/data/<int:ndata>")
def data(ndata=100):
    """
    On request, this returns a list of ``ndata`` randomly made data points.

    :param ndata: (optional)
        The number of data points to return.

    :returns data:
        A JSON string of ``ndata`` data points.

    """
    x = 10 * np.random.rand(ndata) - 5
    y = 0.5 * x + 0.5 * np.random.randn(ndata)
    A = 10. ** np.random.rand(ndata)
    c = np.random.rand(ndata)
    return json.dumps([{"_id": i, "x": x[i], "y": y[i], "area": A[i],
        "color": c[i]}
        for i in range(ndata)])

@app.route("/gdata")
@app.route("/gdata/<float:mux>/<float:muy>")
def gdata(ndata=100,mux=.5,muy=0.5):
    """
    On request, this returns a list of ``ndata`` randomly made data points.
    about the mean mux,muy

    :param ndata: (optional)
        The number of data points to return.

    :returns data:
        A JSON string of ``ndata`` data points.

    """

    """Instead of getting values from URL, try from request object"""
    mux = request.args.get('mux', '')
    muy = request.args.get('muy', '')

    x = np.random.normal(mux,.5,ndata)
    y = np.random.normal(muy,.5,ndata)
    A = 10. ** np.random.rand(ndata)
    c = np.random.rand(ndata)
    return json.dumps([{"_id": i, "x": x[i], "y": y[i], "area": A[i],
        "color": c[i]}
        for i in range(ndata)])

@app.route("/holedata")
def holedata():
    """
    On request, this returns a list of ``ndata`` randomly made data points.
    about the mean mux,muy

    :param ndata: (optional)
        The number of data points to return.

    :returns data:
        A JSON string of ``ndata`` data points.

    """
    csv.reader('')
    out = []
    keys = [
"hole_id","sub_area_id","hole_type_id","hole_design_id","equipment_id","name","depth","time_start","time_end","drilling_time","collar_elevation","heading","mast_angle","start_h_accuracy","start_v_accuracy","end_h_accuracy","end_v_accuracy","validity","start_position","end_position","hole_profile_id","hole_id","time_start","time_end","start_depth","end_depth","frequency","force_on_bit","torque","rop","air_pressure","vibration","blastability","rock_type_id","work_reason_id" ]
    with open('131111-holeid-hole-profile-no-heading.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        out = [dict(zip(keys, property)) for property in reader]
        #for row in reader:
        #   print ', '.join(row)
    #return json.dumps([{"_id": i, "x": x[i], "y": y[i], "area": A[i],
    #    "color": c[i]}
    #    for row in spamreader])
    #keys =
    jsonstr = json.dumps(out)
    print jsonstr
    return jsonstr


if __name__ == "__main__":
    import os

    port = 8000

    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}/".format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)
