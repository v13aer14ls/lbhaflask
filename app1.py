# coding=utf8

from flask import Flask

app1 = Flask(__name__)

@app1.route("/")
def hello_world():
    return "<p>OLA MANOLOS</p>"

if __name__ == '__main__':
   app1.run(debug=True, host='0.0.0.0')
