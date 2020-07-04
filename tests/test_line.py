# coding=utf-8
"""Line feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from puzzle.line import Line


@pytest.fixture(scope='function')
def context():
    return {}


@scenario('line.feature', 'Allowed combinations of values')
def test_allowed_combinations_of_values():
    """Allowed combinations of values."""
    pass


@scenario('line.feature', 'Disallowed combinations of values')
def test_disallowed_combinations_of_values():
    """Disallowed combinations of values."""
    pass


@given('I have a line')
def i_have_a_line(context):
    """I have a line."""
    context["line"] = Line()


@given('I populate the line with <values>')
def i_populate_the_line_with_values(context, values):
    """I populate the line with <values>."""
    context["line"].set_values(values)


@when('I validate the line')
def i_validate_the_line(context):
    """I validate the line."""
    is_valid = context["line"].validate()
    context["is_valid"] = is_valid


@then('The line should be valid')
def the_line_should_be_valid(context):
    """The line should be valid."""
    assert context["is_valid"]


@then('The line should not be valid')
def the_line_should_not_be_valid(context):
    """The line should not be valid."""
    assert not context["is_valid"]

