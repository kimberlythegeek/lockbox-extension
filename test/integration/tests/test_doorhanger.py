"""Tests for the door hanger."""


def test_door_hanger_interaction(fxa_account, login_page):
    """Add an entry and test it shows in the door hanger."""
    fxa = fxa_account
    home_page = login_page.sign_in(fxa.email, fxa.password)
    new_entry = home_page.create_new_entry()

    new_entry.set_site_name('Tuna, Inc.')
    new_entry.set_site_url('https://satuna.org')
    new_entry.set_username('tuna4life')
    new_entry.set_password('tunafish')
    new_entry.set_note('The tuna swim at midnight')
    new_entry.save()

    lists = home_page.door_hanger.find_entrys()
    assert 'Tuna, Inc.' in lists[0].title
    entry = lists[0].click()
    assert 'Tuna, Inc.' in entry.title
