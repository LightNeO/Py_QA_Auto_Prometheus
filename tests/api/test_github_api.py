import pytest
from modules.api.clients.github import Github


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    user = github_api.get_user('def23unk123t')
    assert user['message'] == 'Not Found'
