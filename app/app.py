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
                image_url = meta_tag["content"]
                r = requests.get(image_url)
                with open('./app/static/images/server_icon.png', 'wb') as f:
                    f.write(r.content)
                    return jsonify("Worked : status 200 OK"), 200
        except KeyError:
            pass