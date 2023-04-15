from flask import Flask, jsonify, request
import json
import random as rnd
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Utility functions
def validate_keys(data_dict, required_keys):
   for key in required_keys:
      if key not in data_dict:
         return False
   return True


# Load the JSON data
with open('data/entries.json', 'r') as f:
    data = json.load(f)


@app.route('/api/search')
@cross_origin()
def search():
   query = request.args.get('q')

   results = [entry for entry in data['entries'] if query.lower() in entry['API'].lower() or query.lower() in entry['Description'].lower()]
   return jsonify(results)


@app.route('/api/random')
@cross_origin()
def random():
   query = request.args.get('quantity')
   quantity = int(query) if query != None else 9
   return jsonify([data['entries'][rnd.randint(0,1000)] for n in range(quantity)])


@app.route('/api/all')
@cross_origin()
def all():
   return jsonify(data['entries'])


# add an api to entries object
@app.route('/api/add', methods=['POST'])
@cross_origin()
def add_api():
   required_keys = {'API', 'Description', 'Auth', 'HTTPS', 'Cors', 'Link', 'Cateogry'}
   data = request.get_json()
   print(data.keys)
   if validate_keys(data, required_keys=required_keys):
      return jsonify(data)
   else:
      return jsonify({
         'error': 'Unprocessable Entity'
      })


@app.route('/api/count')
@cross_origin()
def count():
   return jsonify(data['count'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
