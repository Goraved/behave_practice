from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.shop.shop_locators import ShopLocators


class ShopPage(BasePage):
    def open_site(self):
        self.open()

    def open_specific_category(self, category: str):
        self.click(*self.get_parametrized_locator(ShopLocators.CATEGORY_BTN, [category]))

    def add_item_to_cart_and_proceed(self):
        self.hover(*ShopLocators.ITEM_NAME_LBL)
        self.click(*ShopLocators.ADD_TO_CART_BTN)
        self.click(*ShopLocators.PROCEED_TO_CHECKOUT_BTN)

    def go_to_the_second_cart_step(self):
        self.click(*ShopLocators.SECOND_CART_STEP_BTN)

    def finish_order_after_registration(self):
        self.click(*(By.CSS_SELECTOR, '#center_column > form > p > button'))
        self.click(*ShopLocators.TERMS_CHECKBOX)
        self.click(*(By.CSS_SELECTOR, '#form > p > button'))
        self.click(*ShopLocators.PAY_WITH_BANK_BTN)
        self.click(*ShopLocators.CONFIRM_ORDER_BTN)

    def open_profile_order_page(self):
        self.click(*ShopLocators.PROFILE_BTN)
        self.click(*ShopLocators.ORDERS_BTN)

    def is_order_present(self):
        return self.is_element_present(*ShopLocators.ORDER_ROW)
