"""
    Ignnore the warning you see from pylint about "UNABLE TO IMPORT FLASK". 
    To run the program from the "my_website" folder run the
    command:
    1. export FLASK_APP=application.py  
    2. python -m flask run

"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def greeting():
    return render_template("index.html")

#Implement the routes below to handle the request 
#for "about" and "projects" pages
@app.route("/about")
def about():
    pass

@app.route("/projects")
def projects():
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')