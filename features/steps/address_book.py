from behave import *


@given('Phone number "{phone_number}" is not added before to the phone book')
def validate_phone_number_notregistered(context, phone_number):

    assert False
    #assert int(phone_number) not in context.phone_book.phone_numbers


@when('I add first name "{first_name}" and last name "{last_name}" with phone number "{phone_number}" to the phone book')
def register_a_new_member(context, first_name, last_name, phone_number):

    details = {'name': first_name, 'last_name': last_name}

    context.phone_book.add_new_number(int(phone_number), details)


@then('"{phone_number}" is successfully added to the phone book')
def validate_successful_registration(context, phone_number):

    assert int(phone_number) in context.phone_book.phone_numbers

