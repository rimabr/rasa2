from flask import Flask, render_template, request, jsonify
import os,sys,requests, json
from random import randint
app = Flask(__name__)





@app.route('/')
def main():
  return render_template('main.html')

@app.route('/chat')
def home1():
  return render_template('index.html')

@app.route('/dachbord')
def home2():
  return render_template('index2.html')

if __name__ == "__main__":
  app.run(debug=True)