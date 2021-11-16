from behave import *

from page_objects.registation.registration_object import RegistrationPage
from page_objects.shop.shop_object import ShopPage


@given('Open site')
def open_site(context):
    context.shop_page = ShopPage(context.driver)
    context.shop_page.open_site()


@given('Open "{category}" category')
def open_t_shirt_category(context, category):
    context.shop_page.open_specific_category(category)


@when('Add item to cart and proceed')
def add_item_to_card_and_proceed(context):
    context.shop_page.add_item_to_cart_and_proceed()


@when('Go to the second cart step')
def go_to_the_second_cart_step(context):
    context.shop_page.go_to_the_second_cart_step()


@when('Register new account')
def register_new_account(context):
    context.registration_page = RegistrationPage(context.driver)
    context.registration_page.register_account()


@when('Finish order after registration')
def finish_order_after_registration(context):
    context.shop_page.finish_order_after_registration()


@when('Open profile orders page')
def open_profile_orders_page(context):
    context.shop_page.open_profile_order_page()


@then('Check at least 1 order present')
def check_one_order_present(context):
    assert context.shop_page.is_order_present(), 'Order missed'
