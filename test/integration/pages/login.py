"""Login page locators and functions."""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base import Base
from pages.home import Home
from pages.util.util import munged_class_name


class Login(Base):
    """Set up the login page locators and functions."""

    _root_level_locator = (By.TAG_NAME, 'html')
    _confirm_password_locator = (By.NAME, 'confirmPassword')
    _continue_locator = (By.CSS_SELECTOR, 'button.{}'.format(
                         munged_class_name('button')))
    _create_account_locator = (By.ID, 'homepage-linkaccount-action-create')
    _fxa_sign_in_locator = (By.CLASS_NAME, '{}'.format(
                            munged_class_name('normal-theme')))
    _get_started_button_locator = (By.CLASS_NAME, '{}'.format(
                                   munged_class_name('primary-theme')))
    _welcome_locator = (By.CLASS_NAME, '{}'.format(
                        munged_class_name('intro')))

    def wait_for_page_to_load(self):
        """Page load wait."""
        self.wait.until(
            lambda s: s.find_element(*self._welcome_locator).is_displayed())
        return self

    def click_get_started(self):
        """Click get started button."""
        self.find_element(*self._get_started_button_locator).click()
        self.selenium.switch_to.window(self.selenium.window_handles[-1])
        return Home(self.selenium, self.base_url).wait_for_page_to_load()

    def sign_in(self, email, password):
        """Fxa sign in."""
        self.find_element(*self._fxa_sign_in_locator).click()
        self.fxa_sign_in(email, password)
        self.selenium.switch_to.window(self.selenium.window_handles[-1])
        return Home(self.selenium, self.base_url).wait_for_page_to_load()

    # --- Keyboard Navigation --- #
    def tab_to_get_started(self):
        """Activate Get Started button using keyboard navigation."""
        elem = self.find_element(*self._root_level_locator)
        get_started = self.find_element(*self._get_started_button_locator)
        elem.send_keys(Keys.TAB)
        # Tab until "Get Started" button is focused
        while self.selenium.switch_to.active_element != get_started:
            elem.send_keys(Keys.TAB)
        # Activate "Get Started" button
        elem.send_keys(Keys.ENTER)
        self.selenium.switch_to.window(self.selenium.window_handles[-1])
        return Home(self.selenium, self.base_url).wait_for_page_to_load()
