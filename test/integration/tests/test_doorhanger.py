"""Tests for the door hanger."""
from time import sleep

def test_door_hanger_interaction(fxa_account, login_page):
    """Add an entry and test it shows in the door hanger."""
    fxa = fxa_account
    home_page = login_page.sign_in(fxa.email, fxa.password)
    entry = home_page.create_empty_entry()

    lists = home_page.door_hanger.find_entrys()
    assert '(no site name)' in lists[0].title
    entry = lists[0].click()
    assert '' in entry.title
