"""Accessibility tests for Lockbox extension for Firefox."""

import pytest

from axe_selenium_python.axe import run_axe


@pytest.mark.accessiblity
@pytest.mark.xfail
def test_login_page_accessibility(login_page):
    """Test login page for accessibility."""
    run_axe(login_page)


@pytest.mark.accessiblity
@pytest.mark.xfail
def test_home_page_guest_accessiblity(login_page):
    """Test guest home page for accessiblity."""
    home_page = login_page.click_get_started()
    run_axe(home_page)


@pytest.mark.accessiblity
@pytest.mark.xfail
def test_home_page_logged_in_accessibility(fxa_account, login_page):
    """Test logged in home page for accessiblity."""
    fxa = fxa_account
    home_page = login_page.sign_in(fxa.email, fxa.password)
    run_axe(home_page)

# --- Tests to Add: --- #

# @pytest.mark.accessiblity
# def test_new_entry_accessibility(home_page):
#    """Test new entry form for accessiblity."""

# @pytest.mark.accessiblity
# def test_entry_detail_accessibility(home_page):
#     """Test entry detail for accessiblity."""

# @pytest.mark.accessiblity
# def test_populated_entry_list_accessibility(home_page):
#     """Test a non-empty entry list for accessiblity."""
