from flask import Flask, render_template,request
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    username = request.form['username']
    response = requests.get(f'https://api.github.com/users/{username}')
    if response.ok:
        user = response.json()
        return render_template('user.html', user=user)
    else:
        return render_template('error.html', message='User not found')


if __name__ == '__main__':
    app.run(debug=True)