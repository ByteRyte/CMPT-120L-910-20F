from flask import Flask
from flask import render_template
import logging
app = Flask(__name__)

#Sets Logging Level, so that the Logged INFO is visible from the Terminal below
app.logger.setLevel(logging.INFO)

@app.route('/')
def home_page():
    app.logger.info("HOME PAGE: This is the default route when opening up the website")
    return render_template('homepage.html')

@app.route('/')
@app.route('/news/')
def news_page():
    app.logger.info("NEWS PAGE: This page lists all current news related to the company")
    return render_template('news.html')

@app.route('/')
@app.route('/aboutus/')
def about_page():
    app.logger.info("ABOUT PAGE: This page declares basic information about the company")
    return render_template('aboutus.html')

@app.route('/')
@app.route('/funfacts/')
def funfacts_page():
    app.logger.info("FACT PAGE: This page lists random details about the company")
    return render_template('funfacts.html')

@app.route('/')
@app.route('/contactus/')
def contact_page():
    app.logger.info("CONTACT PAGE: This page establishes a list of possible methods to contact the company")
    return render_template('contactus.html')

#Handles 404 Error
@app.errorhandler(404)
def not_found(e):
    app.logger.info("404 PAGE: Something went wrong, and this page shouldn't have been accessed")
    return render_template('error404.html')
