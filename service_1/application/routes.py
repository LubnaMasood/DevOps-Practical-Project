from application import app 
from flask import Flask, request, render_template, jsonify, Response
import requests

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/prizegenerator', methods=['GET','POST'])
def prizegenerator():
    diceroll = requests.get('http://service_2:5000/randomnumber').text
    word_wheel = requests.get('http://service_3:5000/randomword').text

    fields = {"randomnumber": diceroll, "randomword": word_wheel}
    prizeamount = requests.post('http://service_4:5000/service_4', json=fields).text
    return render_template('prizegenerator.html', diceroll=diceroll, word_wheel=word_wheel, prizeamount=prizeamount)
