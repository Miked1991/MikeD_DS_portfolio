from flask import Flask, render_template, request
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager

app=Flask(__name__)

@app.route("/")
def display_home():
  return render_template("index.html")

if "__name__" == "__main__":
  app.run(debug=True)