from flask import Flask, render_template,request,flash
from constants import *
import requests
import json

app = Flask(__name__)


@app.route("/")
def index():
    if request.method == "GET":
        return render_template("index.html")


@app.route("/dictionary-search", methods=["POST"])
def externaldictapicall():
    if request.method == "POST":
        try:
            word = request.form.get("keyword")
            response = requests.get(url=URL.format(word), headers=HEADERS)
            response = json.loads(response.text)["definitions"]
            print(response)
            return render_template("index.html",response=response,keyword=word)
        except Exception as e :
            return render_template("index.html",message= "No Result Not For Entered Keyword {} ".format(word), keyword=word)



if __name__ == "__main__":
    app.run(port=5000)
