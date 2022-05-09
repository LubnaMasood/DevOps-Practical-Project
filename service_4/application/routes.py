from application import app 
from flask import Flask, Response, request, jsonify
import requests

@app.route('/service_4', methods=["GET", "POST"])
def service_4():
    winnerslist = ["football", "swimming swimming", "cricket cricket cricket", "netball netball netball", "golf golf golf golf", "surfing surfing surfing surfing", "basketball basketball basketball basketball", "boxing boxing boxing", "athletics athletics athletics", "badminton badminton badminton",  "rugby rugby rugby",  "iceskating iceskating iceskating"]
    prizestring = " "
    
    if any(ele in randomword for ele in winnerslist) and randomnumber == "1":
        prizestring = 500

    elif any(ele in randomword for ele in winnerslist) and randomnumber == "2":
        prizestring = 1000
    
    elif any(ele in randomword for ele in winnerslist) and randomnumber == "3":
        prizestring = 1500
    
    elif any(ele in randomword for ele in winnerslist) and randomnumber == "4":
        prizestring = 2000 

    elif any(ele in randomword for ele in winnerslist) and randomnumber == "5":
        prizestring = 2500

    elif any(ele in randomword for ele in winnerslist) and randomnumber == "6":
        prizestring = 3000

    elif any(ele in randomword for ele in winnerslist) and randomnumber == "7":
        prizestring = 3500

    elif any(ele in randomword for ele in winnerslist) and randomnumber == "8":
        prizestring = 4000

    elif any(ele in randomword for ele in winnerslist) and randomnumber == "9":
        prizestring = 4500
    
    elif any(ele in randomword for ele in winnerslist) and randomnumber == "10":
        prizestring = 5000
    
    elif any(ele in randomword for ele in winnerslist) and randomnumber == "11":
        prizestring = 5500
    
    elif any(ele in randomword for ele in winnerslist) and randomnumber == "12":
        prizestring = 6000
    else: 
        prizestring = "0"
    data = {"randomsport": randomsport, "diceroll": diceroll, "prizeamount": prizestring}
    return jsonify(data)
