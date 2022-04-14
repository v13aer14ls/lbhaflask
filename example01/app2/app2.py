# coding=utf8

from flask import Flask

app2 = Flask(__name__)

@app2.route("/")
def hello_world():
    return "<p>OLA MANOLOS</p>"

if __name__ == '__main__':
   app2.run(debug=True, host='0.0.0.0')
