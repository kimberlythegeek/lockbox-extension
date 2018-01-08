"""Test for lockbox extension using keyboard navigation only."""


def test_guest_login_with_keyboard(login_page):
    """Log in to Lockbox using keyboard navigation."""
    home_page = login_page.tab_to_get_started()
    assert home_page.sign_in_button_is_displayed()


def test_add_entry_as_guest_with_keyboard(home_page_keyboard):
    """Add a new entry using keyboard navigation."""
    home_page_keyboard.add_entry_using_keyboard()
    assert len(home_page_keyboard.entrires) == 1
    assert '(no site name)' in home_page_keyboard.entries[0].name
