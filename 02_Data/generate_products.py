# ==========================================
# generate_products.py
#
# Purpose:
# Generate product master data.
# Products are assigned to existing suppliers.
# ==========================================


import random
import pandas as pd


from config import (
    NUMBER_OF_PRODUCTS,
    PRODUCT_CATEGORIES
)


from csv_writer import save_to_csv


from data_generator import (
    fake,
    generate_sku,
    generate_price,
    generate_status,
    SEED_VALUE
)



# Make random selection reproducible

random.seed(SEED_VALUE)



# ------------------------------------------
# Generate products
# ------------------------------------------

def generate_products():


    products = []


    # Read supplier data

    suppliers_df = pd.read_csv(
        "../03_Raw_Data/suppliers.csv"
    )


    supplier_ids = (
        suppliers_df["SupplierID"]
        .tolist()
    )



    for product_id in range(
        1,
        NUMBER_OF_PRODUCTS + 1
    ):


        product = {


            "ProductID":

                product_id,


            "ProductName":

                fake.catch_phrase(),


            "SKU":

                generate_sku(),


            "Category":

                random.choice(
                    PRODUCT_CATEGORIES
                ),


            "SupplierID":

                random.choice(
                    supplier_ids
                ),


            "UnitPrice":

                generate_price(),


            "IsActive":

                generate_status()

        }


        products.append(
            product
        )


    return pd.DataFrame(
        products
    )



# ------------------------------------------
# Run generator
# ------------------------------------------

if __name__ == "__main__":


    products_df = generate_products()


    save_to_csv(
        products_df,
        "products.csv"
    )


    print(
        "Product data generation completed."
    )
    
    