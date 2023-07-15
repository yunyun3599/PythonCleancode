import requests
import pymysql
from unittest import mock

ENDPOINT = "url.of.endpoint"


class DBConnection:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost",
                                    user="root",
                                    password="1234",
                                    db="test",
                                    port=3306,
                                    use_unicode=True,
                                    charset="utf8")

    def get_data(self, query):
        with self.conn.cursor() as cur:
            cur.execute(query=query)
            result = cur.fetchone()
        return result


class Delivery:
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
    def send_status(cls, item_id):
        delivery_info = cls.get_status(item_id=item_id)
        delivery_status = {
            "id": item_id,
            "status": delivery_info["status"],
            "update_time": delivery_info["update_time"]
        }
        response = requests.post(ENDPOINT, json=delivery_status)
        response.raise_for_status()
        return response


@mock.patch("mock_patch_delivery_example.requests")
def test_delivery_status_send(mock_request):
    status = 'on_delivery'
    update_time = '2023-07-15 00:00:00'
    mock_status = {"status": status, "update_time": update_time}
    with mock.patch('mock_patch_delivery_example.Delivery.get_status', return_value=mock_status):
        Delivery.send_status(1)

    expected_payload = {"id": 1, "status": status, "update_time": update_time}
    mock_request.post.assert_called_with(ENDPOINT, json=expected_payload)
