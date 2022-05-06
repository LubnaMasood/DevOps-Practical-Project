from application import app 
from flask import Flask, redirect, request, url_for, render_template, jsonify
import requests

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/prizegenerator', methods=['GET','POST'])
def prizegenerator():
    service_2 = requests.get('http://service_2:5000/get_randomnumber').text
    service_3 = requests.get('http://service_3:5000/get_randomword').text

    fields = {"service_2": service_2, "service_3": service_3}
    service_4 = requests.get('http://service_4:5000/service_4').text
    return render_template('prizegenerator.html')
