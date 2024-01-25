from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)

slots_vector = ["",""]
prev_state = [""]
count = [0]

@app.post("/predict")
def predict():
     text = request.get_json().get("message")
     response = get_response(text,slots_vector,count,prev_state)
     prev_state[0] = slots_vector[1]
     message = {"answer":response}
     return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)
