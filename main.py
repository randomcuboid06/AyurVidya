from flask import render_template, Flask, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return redirect(url_for('afterlogin'))

@app.route('/afterlogin', methods=['GET', 'POST'])
def afterlogin():
    return render_template('afterlogin.html')

if __name__ == "__main__":
    app.run(debug=True)