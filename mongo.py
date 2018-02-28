import pymongo
import urllib2
import json
from flask import Flask, render_template, request, session, redirect

connection = pymongo.MongoClient('homer.stuy.edu')
connection.drop_database('neverGonnaGifYouUp')
db = connection.neverGonnaGifYouUp
collection = db.gifs
u = urllib2.urlopen("http://api.giphy.com/v1/gifs/search?q=happy&api_key=dc6zaTOxFJmzC")
x = u.read()
data = json.loads(x)
data = data['data']
collection.insert_many(data)

list_of_gifs = {}
url_to_display = ''
for gif in collection.find({'type':'gif'},{'_id':0, 'title':1, 'url':1}):
    #print gif['title']
    list_of_gifs[gif['title']] = gif['url']

#print list_of_gifs

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('form.html', list_of_gifs = list_of_gifs)
    
@app.route('/display')
def display():
    url_to_display = request.args['gif_name']
    return render_template('gif.html', url = url_to_display)


if __name__ == '__main__':
    app.debug = True
    app.run()
