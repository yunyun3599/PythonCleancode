import random


class ErrorAlertClient:
    """오류 발생 메시지 전송 클라이언트"""

    def send(self, error_channel, error_msg):
        if not isinstance(error_channel, str):
            raise TypeError("error_channel로 문자열 타입을 사용해야 함")
        if not isinstance(error_msg, str):
            raise TypeError("error_msg로 문자열 타입을 사용해야 함")

        print(f"{error_channel} 채널에 {error_msg} 오류 발생")


class Process:
    def __init__(self):
        self.client = ErrorAlertClient()
        self.channel = "channel_1"

    def process_iteration(self, n_interations):
        for i in range(n_interations):
            result = self.run_process()
            self.client.send(self.channel, result)

    def run_process(self):
        result_value = ["abc", "가나다", 0.1, 3]
        return random.choice(result_value)


if __name__ == "__main__":
    process = Process()
    process.process_iteration(4)

