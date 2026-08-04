# ==========================================
# Purpose:
# Generate supplier master data
# and save it as suppliers.csv
# ==========================================

import pandas as pd

from config import NUMBER_OF_SUPPLIERS
from csv_writer import save_to_csv
from data_generator import fake


def generate_suppliers():

    suppliers = []

    for supplier_id in range(1, NUMBER_OF_SUPPLIERS + 1):

        supplier = {

            "SupplierID": supplier_id,

            "SupplierName": fake.company(),

            "ContactName": fake.name(),

            "Email": fake.company_email(),

            "PhoneNumber": fake.phone_number(),

            "Country": fake.country(),

            "IsActive": 1

        }

        suppliers.append(supplier)


    return pd.DataFrame(suppliers)



if __name__ == "__main__":

    suppliers_df = generate_suppliers()

    save_to_csv(
        suppliers_df,
        "suppliers.csv"
    )

    print("Supplier data generation completed.")