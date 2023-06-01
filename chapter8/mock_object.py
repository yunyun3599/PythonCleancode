from typing import List, Dict
from unittest.mock import Mock


class GitBranch:
    def __init__(self, commits: List[Dict]):
        self._commits = {c["id"]: c for c in commits}

    def __getitem__(self, commit_id):
        return self._commits[commit_id]

    def __len__(self):
        return len(self._commits)


def author_by_id(commit_id, branch):
    return branch[commit_id]["author"]


def test_find_commit():
    branch = GitBranch([{"id": "123", "author": "dev1"}])
    assert author_by_id("123", branch) == "dev1"


def test_find_any():
    # GitBranch 함수는 magic method를 사용했기 때문에 Mock 사용이 불가능
    author = author_by_id("123", Mock()) is not None