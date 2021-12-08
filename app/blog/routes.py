from flask import Blueprint, render_template

# create instance of blueprint
blog = Blueprint('blog', __name__, template_folder='blog_templates')

@blog.route('/blog/main')
def bloghome():
    return render_template('blog.html')