from lettuce import step, world
from nose.tools import assert_equals


@step("I am on the Asayer")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    world.browser.get("http://www.asayer.io")


@step("I open the products page")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    element = world.browser.find_element_by_css_selector("a[href='product.html']")
    element.click()


@step("I should see the product details page")
def step_impl(step):
    """
    :type step: lettuce.core.Step
    """
    title = world.browser.title
    assert_equals(title, "QA-as-a-Service | Asayer")
