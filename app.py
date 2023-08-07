from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = a + b
    return f"The sum of {a} and {b} is {result}"

if __name__ == '__main__':
    app.run()
