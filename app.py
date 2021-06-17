'''
from flask import Flask, request, make_response
'''

from flask import Flask,request, make_response,jsonify
app = Flask(__name__)

@app.route("/")
def hello2():
    return "Hello2 again, Universal!"

@app.route('/testme')
def home():
    return 'success'


if __name__=='__main__':
    app.run(debug=True)
