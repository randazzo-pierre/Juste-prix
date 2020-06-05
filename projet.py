#!/usr/bin/env python
# -*- coding: utf­-8 ­-*-

import requests
import json
import random
from flask import Flask, render_template, request
import time

app = Flask(__name__)


@app.route("/", methods = ['get','post'])
def play_game():
    try:
        start_time = time.time()
        print("le juste prix")
        guess = float(request.form['guess'])
        price = float(request.form['price'])
        img = request.form['img']
        name = request.form['name']
        result = None
        count = int(request.form['count'])
        if guess < price:
            result = ("c'est plus.")
            count += 1
        elif guess > price:
            result = ("C'est moins.")
            count += 1
        elif guess == price:
            end_time = time.time() - start_time
            count += 1
            result = ("Bravo réussi en " + str(count) + " essaie et " + str(end_time) + " ")
        return render_template("hello.html", Price=price, Img=img, Name=name, result=result, count=count)
    except:
        count = 0

        numberpage = random.randint(0, 9)
        url = "https://api.cdiscount.com/OpenApi/json/Search"
        params = {
            "ApiKey": '8da2bbcc-ad59-45fb-8116-ecb282c20c76',
            "SearchRequest": {"Keyword": "cuisine",
                              "Pagination": {"ItemsPerPage": 10, "PageNumber": numberpage},
                              "Filters": {"Price": {"Min": 1, "Max": 0},
                                          "Navigation": "cuisine",
                                          "IncludeMarketPlace": "false"}}}

        response = requests.post("https://api.cdiscount.com/OpenApi/json/Search", data=json.dumps(params))

        numberO = random.randint(0, 9)

        price = response.json()['Products'][numberO]['BestOffer']['SalePrice']
        img = response.json()['Products'][numberO]['MainImageUrl']
        name = response.json()['Products'][numberO]['Name']

        price = float(price)
        print(price)
        print(img)
        print(name)

        return render_template("hello.html", Price=price, Img=img, Name=name, count=count)

if __name__=='__main__':
    app.run()
