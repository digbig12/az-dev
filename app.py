from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Aayushi - 2201331560003'

if __name__ == '__main__':
    app.run(port=5000)
