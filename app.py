from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# In-memory storage for our JSON object
json_data = {}

@app.route('/')
def index():
    return render_template('index.html', json_data=json_data)

@app.route('/add', methods=['POST'])
def add_item():
    key = request.form.get('key')
    value = request.form.get('value')
    json_data[key] = value
    return render_template('json-display.html', json_data=json_data)

if __name__ == '__main__':
    app.run(debug=True)