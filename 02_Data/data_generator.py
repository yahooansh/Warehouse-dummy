# ==========================================
# Purpose:
# Reusable functions for generating
# warehouse analytics data.
# ==========================================


import random
import string
from faker import Faker


# ==========================================
# Random Seed Configuration
# ==========================================

SEED_VALUE = 892000

random.seed(SEED_VALUE)

fake = Faker()
fake.seed_instance(SEED_VALUE)


# ------------------------------------------
# Generate random email
# ------------------------------------------

def generate_email(company_name=None):

    if company_name:
        clean_name = (
            company_name
            .lower()
            .replace(" ", "")
        )

        return f"{clean_name}@example.com"

    return fake.email()


# ------------------------------------------
# Generate phone number
# ------------------------------------------

def generate_phone():

    return fake.phone_number()


# ------------------------------------------
# Generate warehouse code
# ------------------------------------------

def generate_warehouse_code(number):

    return f"WH{number:03d}"


# ------------------------------------------
# Generate SKU code
# ------------------------------------------

def generate_sku():

    letters = ''.join(
        random.choices(
            string.ascii_uppercase,
            k=3
        )
    )

    numbers = random.randint(
        10000,
        99999
    )

    return f"{letters}-{numbers}"


# ------------------------------------------
# Generate random price
# ------------------------------------------

def generate_price():

    return round(
        random.uniform(5, 5000),
        2
    )


# ------------------------------------------
# Generate inventory quantity
# ------------------------------------------

def generate_quantity():

    return random.randint(
        0,
        1000
    )


# ------------------------------------------
# Generate active status
# ------------------------------------------

def generate_status():

    return random.choice(
        [1, 1, 1, 0]
    )