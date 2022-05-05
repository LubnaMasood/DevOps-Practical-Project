from application import app 
from flask import Flask, redirect, request, url_for, render_template
import requests, jsonify

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/prizegenerator', methods=['GET','POST'])
def prizegenerator():
    service_2 = requests.get('http://service_2:5000/get_randomnumber').jsonify
    service_3 = requests.get('http://service_3:5000/get_randomword').jsonify
    return render_template('prizegenerator.html', prize=prize)
    