import random
import unittest
from unittest.mock import Mock
from unittest_example_1 import ErrorAlertClient


class WrappedClient:
    def __init__(self):
        self.client = ErrorAlertClient()

    def send(self, error_channel, error_msg):
        return self.client.send(str(error_channel), str(error_msg))


# class Process:
#     def __init__(selsf):
#         self.client = WrappedClient()
#         self.channel = "channel_1"
#
#     def process_iteration(self, n_interations):
#         for i in range(n_interations):
#             result = self.run_process()
#             self.client.send(self.channel, result)
#
#     def run_process(self):
#         result_value = ["abc", "가나다", 0.1, 3]
#         return random.choice(result_value)


class TestWrappedClient(unittest.TestCase):
    def test_send_converts_types(self):
        wrapped_client = WrappedClient()
        wrapped_client.client = Mock()
        wrapped_client.send("value", 1)
        wrapped_client.client.send.assert_called_with("value", "1")

