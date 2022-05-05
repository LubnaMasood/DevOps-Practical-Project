from application import app 
from flask import Flask, Response, request 
import requests, jsonify 

@app.route('/service_4', methods=["GET", "POST"])
def service_4():
    diceroll = requests.get('http://service_2:5000/get_randomnumber').text
    randomsport = requests.get('http://service_3:5000/get_randomword').text
    winnerslist = ["football football", "swimming swimming", "cricket cricket cricket", "netball netball netball", "golf golf golf golf", "surfing surfing surfing surfing"]
    prizestring = " "
    
    if any(ele in randomsport for ele in winnerslist) and diceroll == "1":
        prizestring = 500

    elif any(ele in randomsport for ele in winnerslist) and diceroll == "2":
        prizestring = 1000
    
    elif any(ele in randomsport for ele in winnerslist) and diceroll == "3":
        prizestring = 1500
    
    elif any(ele in randomsport for ele in winnerslist) and diceroll == "4":
        prizestring = 2000 

    elif any(ele in randomsport for ele in winnerslist) and diceroll == "5":
        prizestring = 2500

    elif any(ele in randomsport for ele in winnerslist) and diceroll == "6":
        prizestring = 3000

    elif any(ele in randomsport for ele in winnerslist) and diceroll == "7":
        prizestring = 3500

    elif any(ele in randomsport for ele in winnerslist) and diceroll == "8":
        prizestring = 4000

    elif any(ele in randomsport for ele in winnerslist) and diceroll == "9":
        prizestring = 4500
    
    elif any(ele in randomsport for ele in winnerslist) and diceroll == "10":
        prizestring = 5000
    
    elif any(ele in randomsport for ele in winnerslist) and diceroll == "11":
        prizestring = 5500
    
    elif any(ele in randomsport for ele in winnerslist) and diceroll == "12":
        prizestring = 6000
    else: 
        prizestring = "0"
    data = {"randomsport": randomsport, "diceroll": diceroll, "prizeamount": prize_string}
    return jsonify(data)
