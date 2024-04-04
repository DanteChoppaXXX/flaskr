from app import app

@app.route('/')
def index():
    return "HELLO, WORLD!"

@app.route('/about')
def about():
    return "<h3>This is the about page</h3>"
