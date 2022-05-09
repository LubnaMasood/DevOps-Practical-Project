from flask import Flask, Response, request
from application import app 
import random
import string


@app.route('/randomnumber', methods=["GET"])
def randomnumber(): 
    ticketnumber_choice = random.randint(1,12)
    randomnumber_string += str(randomnumber)
    return Response(f"{randomnumber_string}", mimetype="text/plain")
