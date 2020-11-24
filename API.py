from flask import Flask, render_template, request
import requests
import json
import csv

app = Flask(__name__)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
data_dict = data[0]
bids = {}
rates = data_dict["rates"]
for bid in rates:
    bids.setdefault(bid['code'],bid['bid'])    


with open("file.csv","w",encoding='utf-8', newline='') as csvfile:
    header = ["currency","code","bid","ask"]
    writer = csv.DictWriter(csvfile, fieldnames=header)
    #csvwriter = csv.writer(csvfile, delimiter=";", headers)

    writer.writeheader()
    
    for curr in data_dict["rates"]:
        writer.writerow({"currency":curr["currency"], "code": curr["code"], "bid":curr["bid"],"ask":curr["ask"]})


@app.route("/", methods=["GET", "POST"])
def currency_calc():
    if request.method == "POST":
        data = request.form
        amount = data.get('amount')
        currency = data.get("currency")
                     
        bid = bids[currency]

        data_conv = float(amount) * float(bid)
        return f"You need to spend {round(float(data_conv),2)} PLN, to buy {float(amount)} {currency}."   
        
        
    return render_template("currency_calculator.html")

if __name__ == "__main__":
    app.run(debug=True)