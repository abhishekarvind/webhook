from flask import Flask, request,jsonify
import json


app= Flask(__name__)

@app.route('/')
def home():
    return "Test"


@app.route('/livechat')
def livechat():
    data= request.get_json(force=True)
    print(data)
    return'ok',200

if __name__ =='__main__':
    app.run(debug=True)