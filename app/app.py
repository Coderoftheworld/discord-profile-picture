#!/usr/bin/env python3
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# Web Page


@app.route("/")
def hello():
    return render_template('index.html')

# RESTful api endpoint


@app.route("/scrape", methods=["POST"])
def scrape():
    code = request.get_json()["invite"]
    invite = requests.get(f"https://discord.gg/{code}").text
    soup = BeautifulSoup(invite, features="html.parser")
    for meta_tag in soup.find_all("meta"):
        try:
            if meta_tag["property"] == "og:image":
                return jsonify(meta_tag["content"]), 200
        except KeyError:
            pass