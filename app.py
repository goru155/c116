# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def me():

    name = "Gauransh" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/Father")
def dad():

    name = "Lalit"
    age = "51" 

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/Mother")
def mom():

    name = "Ritu" 
    age = "46" 

    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/Friend")
def bro():

    name = "Ayush" 
    age = "16" 

    return render_template('friend.html' , name = name , age = age)

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
