from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from random import randint
import os
import game

app = Flask(__name__)
app.config["DEBUG"] = True
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

bootstrap = Bootstrap(app)

print(game.chosen)                  # to check

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/how_to/")
def how_to():
    return render_template("how_to.html")

@app.route("/exampletxt/")
def exampletxt():
    return render_template("exampletxt.html")

@app.route("/game/")
def game_web():    
    return render_template("game.html")

@app.route("/upload/")
def upload():
    return render_template("upload.html")

@app.route("/play/")
def play():
    #game.print_all_words_from_database()           ???????
    return render_template("play.html")

@app.route("/upload_completed/", methods=['POST'])
def upload_complete():
    target = os.path.join(APP_ROOT, 'user/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = "user_file" + ".txt"
        destination = "/".join([target, filename])
        file.save(destination)
    return render_template("upload_completed.html")


if __name__ == "__main__":
    app.run()
    #app.run(host="0.0.0.0", port="5000")
    #app.jinja_env.globals.update(play=play)