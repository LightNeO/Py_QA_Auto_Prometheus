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


@pytest.mark.api
def test_search_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_search_repo_cannot_be_found(github_api):
    r = github_api.search_repo('r1b1c1x2')
    assert r['total_count'] == 0


@pytest.mark.api
def test_search_repo_with_single_char(github_api):
    r = github_api.search_repo('q')
    assert r['total_count'] != 0
