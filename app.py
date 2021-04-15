# Let's break down what this code is doing. The first line says that we'll use Flask to render a template, redirecting to another url, and creating a URL. The second line says we'll use PyMongo to interact with our Mongo database. The third line says that to use the scraping code, we will convert from Jupyter notebook to Python.
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# Set up Flask
app = Flask(___name___)

# Use flask_pymongo to set up mongo connection
# This line tells Python that our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL.
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_app'
#is the URI we'll be using to connect our app to Mongo. This URI is saying that the app can reach Mongo through our localhost server, using port 27017, using a database named "mars_app".
mongo = PyMongo(app)

# Define our route for the HTML page. This function is what links our visual representation of our work, our web app, to the code that powers it.
@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)

# Our next function will set up our scraping route. This route will be the "button" of the web application, the one that will scrape updated data when we tell it to from the homepage of our web app. It'll be tied to a button that will run the code when it's clicked.
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)
# Let's look at these six lines a little closer.
# -The first line, @app.route(“/scrape”) defines the route that Flask will be using. This route, “/scrape”, will run the function that we create just beneath it.
# -The next lines allow us to access the database, scrape new data using our scraping.py script, update the database, and return a message when successful. Let's break it down.
# -First, we define it with def scrape():.
# -Then, we assign a new variable that points to our Mongo database: mars = mongo.db.mars.
# -Next, we created a new variable to hold the newly scraped data: mars_data = scraping.scrape_all(). In this line, we're referencing the scrape_all function in the scraping.py file exported from Jupyter Notebook.

if __name__ == "__main__":
   app.run()