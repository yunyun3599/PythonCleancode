class NonDataDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return "descriptor value"


class ClientClass:
    descriptor = NonDataDescriptor()


if __name__ == "__main__":
    client = ClientClass()

    print("###### 초기 상태 ######")
    print(client.descriptor)  # 디스크립터 __get__ 메서드 리턴값 출력
    print(vars(client))  # 객체의 사전 조회

    print("\n###### 객체 사전에 동일한 디스크립터와 동일한 이름으로 속성 등록 ######")
    client.descriptor = "new_val"  # 객체의 사전에 속성 등록
    print(vars(client))  # client 객체의 속성 조회
    print(client.descriptor)  # 객체의 속성 조회

    print("\n###### 객체 속성 삭제 ######")
    del client.descriptor  # 객체의 속성 삭제
    print(vars(client))  # client 객체의 속성 조회
    print(client.descriptor)  # 다시 비데이터 디스크립터 값 조회 -> 'descriptor value'