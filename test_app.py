import json
import pytest
from index import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_status_code(client):
    response = client.post('/')
    assert response.status_code == 200

def test_custom_field(client):
    request_payload = {
        "custom_fields": [
            {
                "tag": "size_in_region",
                "fields": [
                        "size_code",
                        "size_group_code"
                    ]
            },
            {
                "tag": "price_buy_net_currency",
                "fields": [
                    "price_buy_net",
                    "currency"
                ]
            }
        ]
    }
    response = client.post('/', data=json.dumps(request_payload),)
    response_data = json.loads(response.data)

    for custom_field in request_payload.get('custom_fields'):
        assert custom_field['tag'] in response_data[0]['items'][0][
            'items'][0]['items'][0].keys()

def test_custom_groupings(client):
    request_payload = {
        "grouping_keys": [
		    "color",
		    "brand",
		    "article_structure"
	    ]
    }
    response = client.post('/', data=json.dumps(request_payload),)
    response_data = json.loads(response.data)

    first, second, third = request_payload['grouping_keys']

    assert first in response_data[0]
    assert second in response_data[0]["items"][0]
    assert third in response_data[0]["items"][0]["items"][0]