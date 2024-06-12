from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sig_in_page = SignInPage()
    sig_in_page.go_to()
    sig_in_page.try_login('test@test.com', 'wrongpass')

    assert sig_in_page.check_title('Sign in to GitHub · GitHub')
    sig_in_page.close()

