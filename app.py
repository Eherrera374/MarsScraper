

#flask setup
from flask import Flask, render_template, redirect
app = Flask(__name__)

# Mongo DB connection

import pymongo

# Create connection variable
conn = 'mongodb://localhost:27017'


client = pymongo.MongoClient(conn)

db = client.mars_db

collection = db.mars_scrape

from scrape_mars import scrape

@app.route("/")

def home():
    scape_dict = collection.find_one()
    return render_template("index.html", dict = scrape_dict)


@app.route("/scrape")
def reload():
    mars_dict = scrape()
    collection.update({"id":1}, {"$set": mars_dict}, upsert= True)
    return redirect ("http://localhost:5000/", code = 302)



if __name__ == '__main__':
    app.run(debug=True)


