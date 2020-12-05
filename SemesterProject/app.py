from flask import Flask
from flask import render_template
app = Flask(__name__)

app = Flask(__name__)

##app.logger.setLevel(logging.INFO)

@app.route('/')
def hello_world():
    app.logger.warning("This is the default route when opening up the website")
    return 'Hello, World!'



@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    app.logger.warning("This is the incomplete route for repeating a name")
    return render_template('hello.html', name=name)

@app.route('/goodbye/')
@app.route('/goodbye/<name>')
def goodbye(name = None):
    app.logger.warning("This is the incomplete route for saying goodbye to a name")
    return render_template('goodbye.html', name=name)
