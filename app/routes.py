from app import app
from flask import render_template


#@app = decorator
@app.route('/')
def home():
    my_list=['Tahina', 'Sumac', 'Zaatar', 'Golani Olive Oil']
    my_second_list = sorted(my_list)
    return render_template('index.html', my_title ='This is the HOME page', name='Asher', my_list=my_second_list)

@app.route('/about')
def iCanNameThisAnything():
    return render_template('about.html', my_title = 'About')

@app.route('/testing')
def test():
    return {'hi': 'there'}