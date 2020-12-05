from flask import Flask
from flask import render_template
app = Flask(__name__)

app = Flask(__name__)

##app.logger.setLevel(logging.INFO)

@app.route('/')
def hello_world():
    app.logger.info("User traveled to the info route.")
    return 'Hello, World!'



@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    app.logger.warning("This page isn't finished yet but we say hello.")
    return render_template('hello.html', name=name)
