from flask import Flask, jsonify, render_template, request
from main import dice_shake

app = Flask("__main__")


@app.route("/", methods=["GET", "POST"])
def Yacht():
    print(request)
    dices = [1, 1, 1, 1, 1]
    if request.method == "POST":
        dices = dice_shake()
        return jsonify({"dices": dices})
    return render_template("Yacht_main.html", dices=dices)


@app.route("/shake", methods=["GET", "POST"])
def shake():
    print("/shake python in")
    dices = [0, 0, 0, 0, 0]
    if request.method == "GET":
        dices = dice_shake()
        return jsonify({"dices": dices})
    return render_template("Yacht_main.html", dices=dices)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5959)
