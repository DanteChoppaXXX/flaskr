from app import app
from flask import render_template
from datetime import datetime


@app.template_filter('clean_date')
def clean_date(dt):
    return dt.strftime('%d, %b, %y')

@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/jinja')
def jinja():

    my_name = "Choppa"

    age = 30

    languages = ['Python', 'C', 'JavaScript', 'Assembly', 'Rust']

    friends = {
        'Tom': 30,
        'Jake': 34,
        'Kate': 23,
        'Matt': 32
    }

    colors = ('Red', 'Green', 'Yellow', 'Blue')

    cool = True

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f"Pulling repo {self.name}"

        def clone(self):
            return f"Cloning into {self.url}"

    my_remote = GitRemote(
        name='Flask Jinja',
        description='Template Design Tutorial',
        url='https://github.com/DanteChoppaXXX/flaskr.git'
    )


    def repeat(x, qty):
        return x * qty
    
    date = datetime.utcnow()

    my_html = "<h1>THIS IS A HTML</h1>"

    mal_code = "<script>alert('You have been hacked!')</script>"

    return render_template('public/jinja.html', my_name=my_name, age=age,
                            languages=languages, friends=friends, colors=colors,
                            cool=cool, GitRemote=GitRemote, repeat=repeat,
                            my_remote=my_remote, date=date, my_html=my_html,
                            mal_code=mal_code
                            )

@app.route('/about')
def about():
    return "<h3>This is the about page</h3>"
