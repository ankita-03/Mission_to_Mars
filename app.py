from flask import Flask, app, render_template, redirect, url_for
from flask_pymongo import Pymongo
import scrape_mars

app = Flask(__name__)
mongo = Pymongo(app, url = "mongodb://localhost:27017/mars_app")

@app.route("/")
def index(): 
    dataset = mongo.db.dataset.find_one()
    return render_template("index.html", dataset=dataset)

@app.route("/scrape")
def scrape():
    dataset = mongo.db.dataset
    mars = scrape_mars.scrape_start()
    dataset.update({}, mars, upsert = True)
    return redirect("/")

if __name__== "__main__" :
    app.run()