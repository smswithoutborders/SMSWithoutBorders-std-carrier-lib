#!/usr/bin/env python3

from helpers import CarrierInformation

import sys
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    if len(sys.argv) < 2:
        logging.info("Usage: python3 main.py [phone number]")
        sys.exit(1)

    ci = CarrierInformation()

    address = sys.argv[1]
    phonenumber_name = ci.get_operator_name(phone_number=address)
    print(phonenumber_name)

    """

    operator_code = "62401" # MTN Cameroon
    phone_number = "+237690826242" # Orange Cameroon

    operator_country = ci.get_country(operator_code=operator_code)
    phonenumber_country = ci.get_country(phone_number=phone_number)

    print("+ operator_country", operator_country)
    print("+ phonenumber_country", phonenumber_country)

    expected_country = "Cameroon"
    assert operator_country == expected_country
    assert phonenumber_country == expected_country

    operator_name = ci.get_operator_name(operator_code=operator_code)
    phonenumber_name = ci.get_operator_name(phone_number=phone_number)

    print("+ operator_name", operator_name)
    print("+ phonenumber_name", phonenumber_name)

    expected_operator_name = "MTN Cameroon"
    expected_phonenumber_name = "Orange"

    assert operator_name == expected_operator_name
    assert phonenumber_name == expected_phonenumber_name
    """
