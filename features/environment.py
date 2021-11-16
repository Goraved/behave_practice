from lib.driver_wrapper import Driver
from lib.utilities import Utilities


def before_all(context):
    context.driver = Driver().get_driver()


def after_scenario(context, scenario):
    if scenario.status in ('failed', 'error'):
        Utilities.get_screenshot(context.driver)
        Utilities.get_html_source(context.driver)


def after_all(context):
    context.driver.quit()
    Utilities.fix_properties(context.driver)
