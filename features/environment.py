# it's basically a file that defines what should happen before/during/after your test runs.

import logging
from phone_book import PhoneBook


def before_all(context):
    context.config.setup_logging()
    # -- SAME-AS:
    # import logging
    # logging.basicConfig(level=context.config.logging_level)


def before_feature(context, feature):
    if feature.name == 'New numbers':
        phone_book = PhoneBook(phone_numbers=[333], address_book={'name': 'mahshad', 'last_name': 'esl'})
        context.phone_book = phone_book
        logging.info(context.phone_book.phone_numbers)



