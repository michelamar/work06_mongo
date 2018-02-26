import pymongo
import urllib2
import json
from Flask import flask

connection = pymongo.MongoClient('homer.stuy.edu')
db = connection.neverGonnaGifYouUp
db.dropDatabase()

db = connection.neverGonnaGifYouUp
collection = db.gifs
u = urllib2.urlopen("http://api.giphy.com/v1/gifs/search?q=happy&api_key=dc6zaTOxFJmzC")
x = u.read()
data = json.loads(x)
data = data['data']
collection.insert_many(data)

@app.route('/')
def root():
    db.collection.find({
    return render_template('form.html')

@app.route('/gif', methods=['POST', 'GET'])
def gif():
    gifname = request.form['gif']
    
