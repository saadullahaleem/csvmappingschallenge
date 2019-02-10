import itertools as it
import json

from flask import Flask, jsonify, request

from utils import _get_list_from_csv

app = Flask(__name__)


@app.route("/", methods=['POST'])
def list_catalog():
    data = {}
    if request.data:
        data = json.loads(request.data)

    price_catalog = _get_list_from_csv('pricat.csv')
    mappings = _get_list_from_csv('mappings.csv')

    custom_fields = data.get('custom_fields', [])
    grouping_keys = data.get('grouping_keys', ['brand', 'article_number', 'color'])

    first, second, third = grouping_keys

    for mapping in mappings:
        sources = mapping['source_type'].split('|')

        for row in price_catalog:
            key = '|'.join([str(row.get(source)) for source in sources])
            if mapping['source'] == key:
                row[mapping['destination_type']] = mapping['destination']

            for field in custom_fields:
                row[field['tag']] = ' '.join([str(row[f]) for f in field.get('fields')])

    grouped_data = [
        {
            first: key1,
            'items': [
                {
                    second: key2,
                    'items': [
                        {
                            third: key3,
                            'items': list(group3)
                        } for key3, group3 in it.groupby(group2, key=lambda x: x[third])
                    ]
                } for key2, group2 in it.groupby(group1, key=lambda x: x[second])
            ]
        } for key1, group1 in it.groupby(price_catalog, key=lambda x: x[first])]

    return jsonify(grouped_data)

