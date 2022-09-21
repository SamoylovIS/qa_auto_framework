from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage

class TextBoxPages(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys()