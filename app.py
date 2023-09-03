from flask import Flask
from flask import request

# request is used for take input in the method

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h>Hello world</h>"

@app.route("/hello_world1")
def hello_world1():
    return "<h>Hello world1</h>"

@app.route("/hello_world2")
def hello_world2():
    return "<h>Hello world2</h>"

@app.route("/test")
def test():
    a =2+2
    return "this is my test function {}".format(a)

@app.route("/test2")
def test2():
    data =request.args.get('x')
    return "This is the data input from our url {}".format(data)    

if __name__=="__main__":
    app.run(host="0.0.0.0")    