from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Bem-vindo à minha API na Azure!"})

@app.route("/dados", methods=["POST"])
def process_data():
    data = request.get_json()
    return jsonify({"received_data": data}), 200

if __name__ == "__main__":
    app.run(debug=True)
