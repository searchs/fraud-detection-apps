# Pecan

Pecan is toy web application for browsing customer data.

## Installation

Pecan is built using Python 3. You will need to install the Flask framework and other dependencies:

```
pip3 install -r requirements.txt
```

## Starting the app

Run Pecan like this:

```
FLASK_APP=main.py flask run
```

You can then access the web front end at [http://localhost:5000/]() and the API endpoint at [http://localhost:5000/api](). 

### Running Tests
Run tests like this:
```
pytest -v
```

Improvements
1.  When no result, return formatted JSON with "Result Count" set to 0