from flask import Flask, request, jsonify
from flask_cors import CORS

import requests
import json
import time

import os
import dotenv

app = Flask(__name__)
CORS = CORS(app, origins="*")

@app.route("/")
def index():
    return "Alamakk, wes running to?"

if __name__ == "__main__":
    app.run(debug=True)