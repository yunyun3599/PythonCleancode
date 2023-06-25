from datetime import datetime
import requests
from unittest import mock

STATUS_ENDPOINT = "url.of.endpoint"


class BuildStatus:
    @staticmethod
    def build_date() -> str:
        return datetime.utcnow().isoformat()

    @classmethod
    def notify(cls, merge_request_id, status):
        build_status = {
            "id": merge_request_id,
            "status": status,
            "build_at": cls.build_date()
        }
        response = requests.post(STATUS_ENDPOINT, json=build_status)
        response.raise_for_status()
        return response


@mock.patch("mock_patch_git_example.requests")
def test_build_notification_sent(mock_requests):
    build_date = "2019-01-01T00:00:01"
    with mock.patch("mock_patch_git_example.BuildStatus.build_date", return_value=build_date):
        BuildStatus.notify(123, "OK")

    expected_payload = {"id": 123, "status": "OK", "build_at": build_date}
    mock_requests.post.assert_called_with(STATUS_ENDPOINT, json=expected_payload)
