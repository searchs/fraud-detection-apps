from flask import json
import random

from main import app


def test_customers_count_with_no_filter():
    """Check all customers are returned when no filter"""
    response = app.test_client().get('/')
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert len(data) == 250


def test_filter_by_first_name():
    """Check result match filter criteria:  first_name"""
    first_name = "Michael"
    response = app.test_client().get('/?first_name={}'.format(first_name))
    data = json.loads(response.get_data(as_text=True))

    count = len(data)
    random_user = random.randint(0, count - 1)

    assert response.status_code == 200
    assert count < 250
    assert first_name in data[random_user]['first_name']


def test_filter_by_age():
    """Check result match filter criteria:  age"""
    age = 49
    response = app.test_client().get('/?age={}'.format(age))
    data = json.loads(response.get_data(as_text=True))

    count = len(data)
    random_user = random.randint(0, count - 1)

    assert response.status_code == 200
    assert count < 250
    assert age == data[random_user]['age']


def test_results_contain_fields_in_result():

    random_user = random.randint(0, 250)
    response = app.test_client().get('/')

    json_data = json.loads(response.get_data(as_text=True))

    assert 'age' in json_data[random_user].keys()
    assert 'company' in json_data[random_user].keys()
    assert 'current_products' in json_data[random_user].keys()
    assert 'date_of_birth' in json_data[random_user].keys()
    assert 'dominant_traits' in json_data[random_user].keys()
    assert 'first_name' in json_data[random_user].keys()
    assert 'gender' in json_data[random_user].keys()
    assert 'has_children' in json_data[random_user].keys()
    assert 'high_propensity_products' in json_data[random_user].keys()
    assert 'id' in json_data[random_user].keys()
    assert 'income' in json_data[random_user].keys()
    assert 'last_name' in json_data[random_user].keys()
    assert 'life_events' in json_data[random_user].keys()
    assert 'marital_status' in json_data[random_user].keys()
    assert 'metrics' in json_data[random_user].keys()
    assert 'agreeableness' in json_data[random_user]['metrics'].keys()
    assert 'conscientiousness' in json_data[random_user]['metrics'].keys()
    assert 'extraversion' in json_data[random_user]['metrics'].keys()
    assert 'neuroticism' in json_data[random_user]['metrics'].keys()
    assert 'openness' in json_data[random_user]['metrics'].keys()
    assert 'profession' in json_data[random_user].keys()
    assert 'tags' in json_data[random_user].keys()
    assert 'title' in json_data[random_user].keys()
    assert 'wealth' in json_data[random_user].keys()
