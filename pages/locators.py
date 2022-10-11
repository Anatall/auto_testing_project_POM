from selenium.webdriver.common.by import By


class BasePageLocators():
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "a.btn[href='/en-gb/basket/']")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, "i.icon-user")


class BasketPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-items > div.row")
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner p")


class LoginPageLocators():
    EMAIL_FIELD = (By.CSS_SELECTOR, "input#id_registration-email")
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input#id_registration-password1")
    PASSWORD_REPEAT_FIELD = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form#register_form")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


# class MainPageLocators():


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESSFUL_MESSAGE_WITH_BOOK_NAME = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) strong")
    MESSAGE_WITH_COST_OF_BASKET = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) strong")
    NAME_OF_BOOK = (By.CSS_SELECTOR, "div.product_main > h1")
    COST_OF_BOOK = (By.CSS_SELECTOR, "div.product_main > p.price_color")
