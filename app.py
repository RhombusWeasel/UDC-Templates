from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# In-memory storage for our JSON object
json_data = {
    "Global": [],
    "Ingress": [],
    "Egress": []
}
with open('schema.json') as f:
    schema_data = json.load(f)

@app.context_processor
def utility_functions():
    def print_in_console(message):
        print(str(message))

    return dict(mdebug=print_in_console)

@app.route('/')
def index():
    return render_template('index.html', json_data=json_data, config=schema_data)

@app.route('/add', methods=['POST'])
def add_item():
    key = request.form.get('key')
    value = request.form.get('value')
    json_data[key] = value
    return render_template('json-display.html', json_data=json_data)

@app.route('/template/<key>', methods=['GET'])
def add_template(key):
    # return the dynamic form as a modal popup
    return render_template('dynamic-form.html', config=schema_data[key], modal=True, section=key)

@app.route('/submit/<key>', methods=['POST'])
def submit(key):
    data = request.form
    json_data[key].append(data)
    print(json.dumps(json_data[key], indent=2))
    return render_template('index.html', json_data=json_data, config=schema_data)

if __name__ == '__main__':
    app.run(debug=True)