from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_basket_item(self):
        assert self.is_not_element_present(*BasketPageLocators.ADD_TO_BASKET_BUTTON), 'There is item in basket'

    def should_be_message_basket_empty(self):
        print(self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_EMPTY).text)
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), 'No message basket empty'
