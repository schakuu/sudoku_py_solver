# coding=utf-8
"""Panel feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from puzzle.panel import Panel


@pytest.fixture(scope='function')
def context():
    return {}


@scenario('panel.feature', 'Allowed combinations of values')
def test_allowed_combinations_of_values():
    """Allowed combinations of values."""
    pass


@scenario('panel.feature', 'Disallowed combinations of values')
def test_disallowed_combinations_of_values():
    """Disallowed combinations of values."""
    pass


@given('I have a panel')
def i_have_a_panel(context):
    """I have a panel."""
    context["panel"] = Panel()


@given('I populate the panel with <values>')
def i_populate_the_panel_with_values(context, values):
    """I populate the panel with <values>."""
    context["panel"].set_values(values)


@when('I validate the panel')
def i_validate_the_panel(context):
    """I validate the panel."""
    is_valid = context["panel"].validate()
    context["is_valid"] = is_valid


@then('The panel should be valid')
def the_panel_should_be_valid(context):
    """The panel should be valid."""
    assert context["is_valid"]


@then('The panel should not be valid')
def the_panel_should_not_be_valid(context):
    """The panel should not be valid."""
    assert not context["is_valid"]
