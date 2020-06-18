from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def Celebal():
    return "Welcome to Celebal Technologies"


@app.route("/multiply/<int:num>", methods=["GET"])
def Multiply_num(num):
    return jsonify({"result": num * 10})


languages = [{"name": "Python"}, {"name": "Java"}]


@app.route("/lang", methods=["POST"])
def add_language():
    language = {"name": request.json["name"]}
    languages.append(language)
    return jsonify({"languages": languages})


if __name__ == "__main__":
    app.run(debug=True)
