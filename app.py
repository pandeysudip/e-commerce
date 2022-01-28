from flask import Flask, request, render_template, redirect, jsonify
import json
import os
from model_param import model_load
from bson import json_util
from pymongo import MongoClient

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
client = MongoClient("mongodb://localhost:27017")
db = client['e-commerce']


# creating collection (add mongo)
all_data = db['all_data']


@app.route('/')
def home():
    # Return the template
    return render_template('home.html')


@app.route('/index.html')
def index():
    # Return the template
    return render_template('index.html')


@app.route('/send', methods=["GET", "POST"])
def predic():
    if request.method == "POST":

        Administrative = request.form.get('Administrative')
        Administrative_Duration = request.form.get("Administrative_Duration")
        Informational = request.form.get('Informational')
        Informational_Duration = request.form.get('Informational_Duration')
        ProductRelated = request.form.get('ProductRelated')
        ProductRelated_Duration = request.form.get('ProductRelated_Duration')
        BounceRates = request.form.get('BounceRates')
        ExitRates = request.form.get('ExitRates')
        PageValues = request.form.get('PageValues')
        variables = [Administrative, Administrative_Duration,
                     Informational, Informational_Duration, ProductRelated,
                     ProductRelated_Duration, BounceRates,
                     ExitRates, PageValues]
        predict = model_load(variables)

        return render_template("index.html", pred=variables, prediction=predict)
    else:
        return render_template("index.html")


@ app.route("/data/all_data")
def all_data():
    all_data_list = list(all_data.find())
    return json.dumps(all_data_list, default=json_util.default)


if __name__ == "__main__":
    app.run(debug=True)
