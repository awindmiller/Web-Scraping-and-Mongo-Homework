from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Mission_to_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    MarsDict = mongo.db.MarsDict.find_one()
    return render_template("index.html", listings=MarsDict)


@app.route("/scrape")
def scraper():
    MarsDict = mongo.db.MarsDict
    MissionData = Mission_to_Mars.scrape()
    MarsDict.update({}, MissionData, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
