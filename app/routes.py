from app import app
from flask import render_template

@app.route('/')
def home():
    my_list = ['Shoha',"Josh", 'Dylan','Nicole']
    my_second_list = sorted(my_list)
    return render_template('index.html', my_title = "This is the HOME page", name='Shoha', my_list = my_second_list)

@app.route('/about')
def iCanNameThisAnything():
    return render_template('about.html', my_title = "aBoUt")

@app.route('/testing')
def test():
    return {'hi':'there'}