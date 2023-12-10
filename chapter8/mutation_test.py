import unittest
from enum import Enum


class MergeRequestStatus(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending"


def evaluate_merge_request(upvote_count, downvotes_count):
    if downvotes_count > 0:
        return MergeRequestStatus.REJECTED
    if upvote_count >= 2:
        return MergeRequestStatus.APPROVED
    return MergeRequestStatus.PENDING


class TestMergeRequestEvaluation(unittest.TestCase):
    def test_approved(self):
        result = evaluate_merge_request(3, 0)
        self.assertEqual(result, MergeRequestStatus.APPROVED)

"""
1. mutpy 설치
$ pip install mutpy

2. mutpy 테스트 실행
$ mut.py \
    --target mutation_test \
    --unit-test mutation_test \
    --operator AOD `# 산술 연산자 삭제` \
    --operator AOR `# 산술 연산자 교체` \
    --operator COD `# 조건 연산자 삭제` \
    --operator COI `# 조건 연산자 추가` \
    --operator CRP `# 상수 교체` \
    --operator ROR `# 관계 연산자 교체` \
    --show-mutants
"""