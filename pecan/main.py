import json

from flask import Flask, jsonify, request

app = Flask(__name__)

customers = json.load(open("customers.json", "r"))


@app.route("/")
def get_customers():
    """Returns list of customers.  Filterable"""
    filtered_customers = filter_by()
    return jsonify(filtered_customers)


def filter_by():
    """Filter result based on request params.  Default is none."""
    filtered_customers = customers

    if request.args:
        terms = request.args
        # Assuming only one argument is passed
        _term, _value = terms.keys(), terms.values()
        filter_term = next(_term)
        filter_value = next(_value)

        if request.args.get(filter_term):
            filtered_customers = [
                c for c in customers if c[filter_term] == filter_value
            ]
            if len(filtered_customers) == 0:
                filtered_customers = {"Results": 0}
    return filtered_customers
