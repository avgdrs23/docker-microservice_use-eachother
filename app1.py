#!/usr/local/bin/python3

from flask import  Flask 
from flask import request

app = Flask("app1")

@app.route("/add")
def add():
 # return '<html><body><h2>Text input fields</h2><form> <label for="fname">Num1:</label><br><input type="number"><label for="fname">Num2:</lab>
   a=int(request.args.get("a"))
   b=int(request.args.get("b"))
   return str(a+b)

   
app.run(port=8081, host="0.0.0.0")
