from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    MSG_WITH_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success:nth-of-type(1) .alertinner')
    MSG_WITH_PROMO = (By.CSS_SELECTOR, '.alert-success:nth-of-type(2) .alertinner')
    MSG_WITH_BASKET_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner p:first-child')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
