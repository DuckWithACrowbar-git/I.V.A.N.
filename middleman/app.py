from flask import Flask, jsonify, request

app = Flask(__name__)

data = None

@app.route("/post", methods=['POST'])
def post():
    global data
    data = request.get_json()
    data = data.get('data')
    return jsonify({"Status": "Success"}), 200

@app.route("/get", methods=['GET'])
def get():
    return jsonify({"data": str(data)})


app.run(host="0.0.0.0", port=1234, debug=False)