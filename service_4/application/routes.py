from application import app 
from flask import Flask, Response, request, jsonify
import requests

@app.route('/service_4', methods=["GET", "POST"])
def service_4():
    randomnumber = int(request.get_json()['randomnumber'])
    randomword = request.get_json()['randomword']
    
    winnerslist = ["football", "swimming", "cricket", "netball", "golf", "surfing", "basketball", "boxing", "athletics", "badminton",  "rugby",  "iceskating"]
    sport= " "
    prizestring=0

    if randomword.startswith('b'):
        if randomnumber==1:
            prizestring=500

        elif randomnumber==2:
            prizestring=1000

        elif randomnumber==3:   
            prizestring=1500

        elif randomnumber==4:   
            prizestring=2000

        elif randomnumber==5:   
            prizestring=2500

        elif randomnumber==6:   
            prizestring=3000

        elif randomnumber==7:   
            prizestring=3500

        elif randomnumber==8:   
            prizestring=4000

        elif randomnumber==9:   
            prizestring=4500

        elif randomnumber==10:   
            prizestring=5000

        elif randomnumber==11:   
            prizestring=5500

        elif randomnumber==12:   
            prizestring=6000
        
    else:
        prizestring="You Loose!"
    #data = {"randomsport": randomsport, "diceroll": diceroll, "prizeamount": prizestring}
    return Response(f"{prizestring}", mimetype="text/plain")
