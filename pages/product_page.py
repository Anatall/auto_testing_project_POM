from .base_page import BasePage
from .locators import ProductPageLocator

class ProductPage(BasePage):
    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocator.BASKET_BUTTON), 'Basket button is not presented'

    def should_be_message_with_product_name(self):
        assert self.is_element_present(*ProductPageLocator.SUCCESSFUL_MESSAGE_WITH_BOOK_NAME), "Can't find successful " \
                                                                                               "message with name of book"

    def should_be_message_cost_of_book(self):
        assert self.is_element_present(*ProductPageLocator.MESSAGE_WITH_COST_OF_BASKET), "Can't find " \
                                                                                         "message with cost of basket"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocator.NAME_OF_BOOK), "Can't find successful name of book"

    def should_be_cost_of_book(self):
        assert self.is_element_present(*ProductPageLocator.COST_OF_BOOK), "Can't find cost of book"

    def add_to_basket(self):
        self.should_be_basket_button()
        button_add_basket = self.browser.find_element(*ProductPageLocator.BASKET_BUTTON)
        button_add_basket.click()

    def compare_names_of_book(self):
        self.should_be_product_name()
        self.should_be_message_with_product_name()
        text_name_book_in_message = self.browser.find_element(*ProductPageLocator.SUCCESSFUL_MESSAGE_WITH_BOOK_NAME).text
        name_of_book = self.browser.find_element(*ProductPageLocator.NAME_OF_BOOK).text
        print(f'expected: {name_of_book}, \n actual: {text_name_book_in_message}')
        print(self.compare_expected_and_actual_results(name_of_book,
                                                        text_name_book_in_message))
        assert self.compare_expected_and_actual_results(name_of_book,
                                                        text_name_book_in_message), f'actual result is not equal to expected;' \
                                                                                    f'actual: {text_name_book_in_message},' \
                                                                                    f'expected: {name_of_book}'

    def compare_cost_of_book_and_basket(self):
        self.should_be_cost_of_book()
        self.should_be_message_cost_of_book()
        text_cost_of_basket = self.browser.find_element(*ProductPageLocator.MESSAGE_WITH_COST_OF_BASKET).text
        cost_of_book = self.browser.find_element(*ProductPageLocator.COST_OF_BOOK).text
        assert self.compare_expected_and_actual_results(cost_of_book,
                                                        text_cost_of_basket), f'actual result is not equal to expected;' \
                                                                                    f'actual: {text_cost_of_basket},' \
                                                                                    f'expected: {cost_of_book}'
