from flask import Flask
from flask import request, redirect
from flask import render_template
import pandas as pd


app = Flask(__name__)

@app.route('/form', methods=['GET'])
def init_form():
       
    return render_template("form.html")

@app.route('/log', methods=['GET', 'POST'])
def init_log():
    if request.method == 'GET':
        print('We received GET')
        return render_template("log.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect("/")

   
    
@app.route('/message', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")
    
