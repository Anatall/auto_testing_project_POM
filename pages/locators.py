from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, 'form#register_form')

class ProductPageLocator():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    SUCCESSFUL_MESSAGE_WITH_BOOK_NAME = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) strong')
    MESSAGE_WITH_COST_OF_BASKET = (By.CSS_SELECTOR, '#messages > .alert:nth-child(3) strong')
    NAME_OF_BOOK = (By.CSS_SELECTOR, 'div.product_main > h1')
    COST_OF_BOOK = (By.CSS_SELECTOR, 'div.product_main > p.price_color')