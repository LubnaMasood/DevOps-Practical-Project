from flask import Flask, Response, request
from application import app 
import random
import string


@app.route('/randomnumber', methods=["GET"])
def randomnumber(): 
    randomnumber_string = random.randint(1,12)
    return Response(f"{randomnumber_string}", mimetype="text/plain")
