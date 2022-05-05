from flask import Flask, Response, request, url_for, redirect, render_template
from application import app 
import random


@app.route('/get_randomnumber', methods=["GET"])
def randomnumber(): 
    randomnumber_string = " "
    ticketnumber_choice = random.randint(1,12)
    randomnumber_string += str(randomnumber)
    return Response(f"{randomnumber_string}", mimetype="text/plain")
