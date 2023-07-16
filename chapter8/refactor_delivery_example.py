import requests
from chapter8.mock_patch_delivery_example import DBConnection
import pytest
from unittest.mock import Mock

ENDPOINT = "url.of.endpoint"


class Transport:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def post(self, payload):
        return requests.post(self.endpoint, json=payload)


class Delivery:
    def __init__(self, transport):
        self.transport = transport

    @staticmethod
    def get_status(item_id: str):
        delivery_info = DBConnection().get_data(
            f"""
            select status, update_time 
              from test.delivery 
             where id={item_id}
            """)
        return {"status": delivery_info[0], "update_time": delivery_info[1].strftime('%Y-%m-%d %H:%M:%S')}

    @classmethod
    def make_payload(cls, item_id):
        delivery_info = cls.get_status(item_id=item_id)
        delivery_status = {
            "id": item_id,
            "status": delivery_info["status"],
            "update_time": delivery_info["update_time"]
        }
        return delivery_status

    def send_request(self, payload):
        response = self.transport.post(ENDPOINT, json=payload)
        response.raise_for_status()
        return response

    def send_status(self, item_id):
        return self.send_request(self.make_payload(item_id=item_id))


@pytest.fixture
def delivery():
    delivery = Delivery(Mock())
    status = 'on_delivery'
    update_time = '2023-07-15 00:00:00'
    mock_status = {"status": status, "update_time": update_time}
    delivery.get_status = Mock(return_value=mock_status)
    return delivery


def test_delivery_status_send(delivery):
    delivery.send_status(item_id="1")
    expected_payload = delivery.make_payload(item_id="1")
    delivery.transport.post.assert_called_with(ENDPOINT, json=expected_payload)

