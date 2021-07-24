import os
from flask import Flask, render_template, request

app = Flask(__name__)
picNum = 0


def newPicture():
    global picNum
    if picNum != 0:
        os.remove('static/picture' + str(picNum) + '.jpg')
    picNum += 1
    os.system('raspistill -o static/picture' + picNum + '.jpg')


@app.route("/", methods=["GET","POST"])
def home():
    global picNum
    newPicture()
    return "<img src='static/picture' + picNum + '.jpg'>"


if __name__ == "__main__":
    #will run on: http://192.168.1.162:8080/
    try:
        app.run(host='0.0.0.0', port=8080, debug=True)
    except KeyboardInterrupt:
        os.remove('static/picture' + str(picNum) + '.jpg')