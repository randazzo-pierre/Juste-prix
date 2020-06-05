#!/usr/bin/env python
# -*- coding: utf­-8 ­-*-

import requests
import json
import random
from flask import Flask
import time
import bs4

app = Flask(__name__)


@app.route("/")
def play_game():
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
    print(json.dumps(response.json(), indent=4))
    price = response.json()['Products'][numberO]['BestOffer']['SalePrice']
    img = response.json()['Products'][numberO]['MainImageUrl']
    name = response.json()['Products'][numberO]['Name']

    print(price)
    print(img)
    print(name)

    start_time = time.time()
    print("le juste prix")
    number = float(price)
    count = 1

    while True:

        guess = float(input("Prix: "))
        if guess < number:
            print("c'est plus.")
        elif guess > number:
            print("C'est moins.")
        elif guess == number:
            end_time = time.time() - start_time
            print("Bravo réussi en " + str(count) + " essaie et " + str(end_time) + " seconde ")
            return
        count += 1


play_game()

if __name__ == "__projet__":
    app.run()
