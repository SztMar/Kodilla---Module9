from flask import Flask, render_template, request
import json



app = Flask(__name__)

#user = {"username": "jamesbond", "password": "superpass123"}
with open('C:\\Kodilla_course\\Module9\\templates\\access_db.json') as f:
    data_json = json.load(f)


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form
        username = data.get('username')
        password = data.get("password")
        username1 = data_json['users'][username]["username"]
        password1 = data_json['users'][username]["password"]
        #if username == user['username'] and password == user["password"]:
            #return "Jesteś w systemie. Wiadomość ulegnie samozniszczeniu... "
        if username == username1 and password == password1:
            return "Jesteś w systemie. Wiadomość ulegnie samozniszczeniu... "

    return render_template("login_form_post.html")
    


if __name__ == "__main__":
    app.run(debug=True)

