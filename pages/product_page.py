from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_add_to_basket_messages(self):
        self.should_be_message_with_product_name(self.get_product_name())
        self.should_be_message_with_promo()
        self.should_be_message_with_basket_price(self.get_product_price())

    def should_be_message_with_product_name(self, product_name):
        assert self.is_element_present(
            *ProductPageLocators.MSG_WITH_PRODUCT_NAME), "Message with product name is not presented"

        expected_message = f'{product_name} has been added to your basket.'
        message_with_product_name = self.browser.find_element(*ProductPageLocators.MSG_WITH_PRODUCT_NAME).text
        self.should_be_expected_message(message_with_product_name, expected_message)

    def should_be_message_with_promo(self):
        assert self.is_element_present(*ProductPageLocators.MSG_WITH_PROMO), "Message with promo is not presented"

        expected_message = 'Your basket now qualifies for the Deferred benefit offer offer.'
        message_with_promo = self.browser.find_element(*ProductPageLocators.MSG_WITH_PROMO).text
        self.should_be_expected_message(message_with_promo, expected_message)

    def should_be_message_with_basket_price(self, product_price):
        assert self.is_element_present(
            *ProductPageLocators.MSG_WITH_BASKET_PRICE), "Message with basket price is not presented"

        expected_message = f'Your basket total is now {product_price}'
        message_with_product_price = self.browser.find_element(*ProductPageLocators.MSG_WITH_BASKET_PRICE).text
        self.should_be_expected_message(message_with_product_price, expected_message)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MSG_WITH_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MSG_WITH_PRODUCT_NAME), \
            "Success message is not disappeared, but should be"
