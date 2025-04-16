from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Beckn Mock API!"})

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    return jsonify({
        "context": data.get("context", {}),
        "message": {
            "catalog": {
                "products": [
                    {"id": "1", "name": "Product A"},
                    {"id": "2", "name": "Product B"}
                ]
            }
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
