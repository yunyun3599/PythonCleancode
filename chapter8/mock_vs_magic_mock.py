from unittest.mock import Mock, MagicMock
from typing import Dict


class UnregisteredCandidateException(Exception):
    pass


class Voting:
    def __init__(self, *candidates: str):
        self._result = {candidate: 0 for candidate in candidates}

    @property
    def result(self) -> Dict:
        return self._result

    def vote(self, candidate: str):
        if candidate in self._result.keys():
            self._result[candidate] = self._result[candidate] + 1
            print(f"{candidate}: {self._result[candidate]}")
            return self._result[candidate]
        else:
            raise UnregisteredCandidateException(f"{candidate}는 등록되지 않은 후보입니다.")

    def __getitem__(self, candidate: str):
        return self._result[candidate]

    def __len__(self):
        return len(self._result)


def get_vote_num(vote: Voting, candidate: str):
    return vote[candidate]


def get_vote_status(vote: Voting):
    return vote.result


def vote_to_candidate(vote: Voting, candidate: str):
    return vote.vote(candidate=candidate)


def test_get_vote_num_with_mock():
    vote = Mock()
    vote.__getitem__.return_value = 0
    assert get_vote_num(vote, "candidate1") == 0


def test_get_vote_num_with_magic_mock():
    vote = MagicMock()
    vote.__getitem__.return_value = 0
    assert get_vote_num(vote, "candidate1") == 0


def test_result_with_mock():
    # 테스트 대상이 매직 메서드가 아니면 Mock 사용 가능
    vote = Mock()
    vote.result = {"candidate1": 10, "candidate2": 20}
    assert get_vote_status(vote) == {"candidate1": 10, "candidate2": 20}


def test_result_with_magic_mock():
    vote = MagicMock()
    vote.result = {"candidate1": 10, "candidate2": 20}
    assert get_vote_status(vote) == {"candidate1": 10, "candidate2": 20}


def test_vote_with_mock():
    vote = Mock()
    vote.vote.return_value = 10
    assert vote_to_candidate(vote, "candidate") == 10


def test_vote_with_magic_mock():
    vote = MagicMock()
    vote.vote.return_value = 10
    assert vote_to_candidate(vote, "candidate") == 10

