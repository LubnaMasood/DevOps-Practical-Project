from flask import Flask, Response, request
from application import app 
import random

@app.route('/randomword', methods=["GET"])
def randomword(): 
   word_choice = ["football", "swimming", "cricket", "netball", "golf", "surfing", "basketball", "boxing", "athletics", "badminton", "rugby", "iceskating"]
   word_choice_selected = random.choice(word_choice)
   return Response(f"{word_choice_selected}", mimetype="text/plain")
