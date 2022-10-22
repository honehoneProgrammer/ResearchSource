from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    hello = "Hello world"
    return hello

@app.route('/test')
def other1():
    return "テストページです！"

if __name__ == "__main__":
    app.run()