from flask import Flask, Response, request
from application import app 
import random

@app.route('/get_randomword', methods=["GET", "POST"])
def randomword(): 
   word_choice = ["football", "swimming", "cricket", "netball", "golf", "surfing"]
   word_1 = random.choice(word_choice)
   word_2 = random.choice(word_choice)
   word_3 = random.choice(word.choice)
   word_4 = random.choice(word.choice)
   word_5 = random.choice(word.choice)
   word_6 = random.choice(word.choice)
   randomword_string = str(word_1 + word_2 + word_3 + word_4 + word_5 + word_6)
   return Response(f"{randomword_string}", mimetype="text/plain")
