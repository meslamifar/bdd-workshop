from behave import *
from phone_book import PhoneBook


@given('a set of phone numbers')
def set_phone_book(context):
    raise NotImplementedError("this part should get implemented")


@when('we search for name "{name}"')
def search_for_name(context, name):
    raise NotImplementedError("this part should get implemented")


@then('we will find two people in "{city}"')
def validate_phone_book_entries(context, city):
    raise NotImplementedError("this part should get implemented")


@then('we will find one person in "{city}"')
def step_impl(context, city):
    raise NotImplementedError("this part should get implemented")
