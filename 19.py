from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello this is index page"

@app.route("/hello")
def sayHello():
    return "Hello mohammad how are you !"

@app.route("/welcome/")
@app.route("/welcome/<id>")
def welcome(id = None):
    message =  "The ID is " + str(id)
    if id is None : message = "Id should not being none !"
    
    return message