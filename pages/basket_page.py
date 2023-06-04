from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_PRODUCTS), 'There are products in basket, but should not be'

    def should_be_message_empty_basket(self):
        self.is_element_present(*BasketPageLocators.MSG_EMPTY_BASKET), 'Message about empty basket is not presented'
        expected_message = 'Your basket is empty.'
        message_empty_basket = self.browser.find_element(*BasketPageLocators.MSG_EMPTY_BASKET).text
        assert expected_message in message_empty_basket, f'Expected that message: "{expected_message}" to be contained in: "{message_empty_basket}"'
