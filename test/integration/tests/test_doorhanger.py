"""Tests for the door hanger."""
from time import sleep

def test_door_hanger_interaction(fxa_account, login_page):
    """Add an entry and test it shows in the door hanger."""
    fxa = fxa_account
    home_page = login_page.sign_in(fxa.email, fxa.password)
    entry = home_page.create_empty_entry()
    #
    # entry.set_site_name('Tuna, Inc.')
    # entry.set_site_url('https://satuna.org')
    # entry.set_username('tuna4life')
    # entry.set_password('tunafish')
    # entry.set_note('The tuna swim at midnight')
    # entry.save()
    # sleep(5)
    lists = home_page.door_hanger.find_entrys()
    print(lists)
    assert 'Tuna, Inc.' in lists[0].title
    entry = lists[0].click()
    assert 'Tuna, Inc.' in entry.title
