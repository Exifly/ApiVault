from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, request
from search import Search
import random as rnd
import datetime
import logging
import json
import os


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


filelog_name = 'apivault-{date:%Y%m%d}.txt'.format(
    date=datetime.datetime.now())
os.makedirs(os.path.dirname(f'log/{filelog_name}'), exist_ok=True)
logging.basicConfig(
    filename=f'log/{filelog_name}.log', filemode="w+", level=logging.INFO)


# Load the JSON data
try:
    with open('data/entries.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    logging.error('File data/entries.json not found')
    raise


@app.route('/api/search')
@cross_origin()
def search():
    """
    1. Get the search query and category from the request arguments
    2. Filter the data entries based on the search query and category
    3. Return the filtered results as a JSON object
    """
    query = request.args.get('q')
    category = request.args.get('category')
    results = Search.search_entries(data['entries'], query, category)

    logging.info(
        f'Search query="{query}" category="{category}" results={len(results)}')
    return jsonify(results)


@app.route('/api/random')
@cross_origin()
def random():
    """
    1. Get the requested quantity from the request arguments
    2. Convert the quantity to an integer if it exists, otherwise use the default value of 9
    3. Generate random data entries and return them as a JSON object
    """
    query = request.args.get('quantity')
    quantity = int(query) if query != None else 9
    entries = rnd.sample(data['entries'], min(quantity, len(data['entries'])))

    logging.info(f'Random request quantity={quantity} results={len(entries)}')
    return jsonify(entries)


@app.route('/api/all')
@cross_origin()
def all():
    """Get all entries """
    categorie = request.args.get('categorie')
    if not categorie:
        return data['entries']
    return jsonify(Search.all_entries(data['entries'], categorie))


@app.route('/api/count')
@cross_origin()
def count():
    """Get the count of entries"""
    return jsonify(len(data.get('entries')))


@app.route('/api/categories/trending')
@cross_origin
def trending_categories():
    category_counts = {}
    for entry in data['entries']:
        category = entry['Category']
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts = 1
    sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse = True)
    top_categories = [{"category_name": category[0], "api_count": category[1]} for category in sorted_categories[:10]]
    response = {
        "trending_categories": top_categories
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
