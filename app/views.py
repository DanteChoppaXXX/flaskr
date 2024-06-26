from app import app
from flask import render_template, request, redirect, url_for, make_response
from datetime import datetime


@app.template_filter('clean_date')
def clean_date(dt):
    return dt.strftime('%d, %b, %y')

@app.route('/')
def index():

    print(app.config["DB_NAME"])

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

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        print(username, email, password)

    return render_template('public/sign_up.html')

@app.route('/profile/<username>')
def profile(username):

    print(username)

    return render_template('public/profile.html')

@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():


    return render_template('public/upload_image.html')


@app.route('/cookies')
def cookies():

    res = make_response("Cookies", 200)

    res.set_cookie(
        "flavor",
         value="chocolate chip",
         max_age=10,
         expires=None,
         path=request.path,
         domain=None,
         secure=False,
         httponly=False,
         
    )

    return res