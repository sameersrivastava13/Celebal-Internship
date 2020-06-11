from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def Celebal():
    return "Welcome to Celebal Technologies"


@app.route("/multiply/<int:num>", methods=["GET"])
def Multiply_num(num):
    return jsonify({"result": num * 10})


if __name__ == "__main__":
    app.run(debug=True)
