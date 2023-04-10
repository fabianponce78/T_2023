'''
Created on Feb 8, 2023

@author: fponce
'''
#from aiohttp._http_parser import method

'''
    See.    https://www.youtube.com/watch?v=fxavwHPJ36o
            https://www.youtube.com/watch?v=Rxp3mkg2mRQ&t=651s
'''
from flask import Flask, render_template

app = Flask(__name__)

# Creating simple Routes 
@app.route('/test')
def test():
    return "Home Page"

@app.route('/test/about/')
def about_test():
    return "About Page"

# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

##############################################################
@app.route('/form_Test')
def form_Test():
    return render_template("form_Test.html")
'''
'''
@app.route('/form_B')
def form_submit():
    V_title = "Thank You!"
    return render_template("form_POST.html", title=V_title)

##############################################################
@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)