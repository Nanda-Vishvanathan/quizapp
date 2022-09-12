from flask import Flask, render_template, request,session
from logic import *

def create_app():
    "Initialize the app with a secret key"
    app = Flask(__name__)
    app.secret_key = "SE" #If production/staging, this shall be changed.
    return app

app = create_app() #Method invocation to initialize the app

@app.route('/')
def index():
    "Forms the base url of the quiz application"
    return render_template('base.html')

@app.route('/stubbenedge/quiz')
def quiz():
    "This snippet makes the call to extract countries and generate the quiz question"
    session.clear()
    country_details,random_result = get_country_details()
    country_quiz = country_details[random_result[0]]
    session['country'] = country_quiz['name']
    session['capital_d'] = country_quiz['capital']
    return render_template('quiz.html', country = session.get('country', 'not set'),capital_d = session.get('capital_d', 'not set'))

@app.route('/stubbenedge/check', methods = ['POST','GET'])
def check():
    "This forms the validation snippet to check if the entered capital is correct or wrong."
    if request.method=='POST':
        capital = request.form['capital']
    if session.get('capital_d', 'not set').lower() == capital.lower():
        message = "Perfect! "+session.get('capital_d', 'not set')+" is indeed the capital of "+session.get('country', 'not set')
    else:
        message = "You missed it! The correct Answer is "+session.get('capital_d', 'not set')
    return render_template('result.html', message=message)   

if __name__ == '__main__':
    app.run(debug=True)
