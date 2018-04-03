"""Test Lockbox for accessibility violations."""

import pytest
from pytest_axe.pytest_axe import run_axe


@pytest.mark.accessibility
def test_login_page_accessibility(login_page):
    """Test login page for accessibility violations."""
    run_axe(login_page, None, None, 'critical')


@pytest.mark.accessibility
def test_home_page_guest_accessibility(home_page):
    """Test home page as guest for accessibility violations."""
    run_axe(home_page, None, None, 'critical')


@pytest.mark.accessibility
def test_home_page_logged_in_accessibility(fxa_account, login_page):
    """Test home page when logged in for accessibility violations."""
    fxa = fxa_account
    home_page = login_page.sign_in(fxa.email, fxa.password)
    run_axe(home_page, None, None, 'critical')
