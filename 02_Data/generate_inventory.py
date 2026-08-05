# ==========================================
# Purpose:
# Generate inventory snapshot data.
# Inventory connects products and warehouses.
# ==========================================


import random
import pandas as pd


from config import (
    NUMBER_OF_INVENTORY_RECORDS,
    INVENTORY_REORDER_LEVELS
)


from csv_writer import save_to_csv


from data_generator import (
    generate_quantity,
    SEED_VALUE
)



# Make random values reproducible

random.seed(SEED_VALUE)



# ------------------------------------------
# Generate inventory
# ------------------------------------------

def generate_inventory():


    inventory = []


    # Read existing master data

    products_df = pd.read_csv(
        "../03_Raw_Data/products.csv"
    )


    warehouses_df = pd.read_csv(
        "../03_Raw_Data/warehouses.csv"
    )



    product_ids = (
        products_df["ProductID"]
        .tolist()
    )


    warehouse_ids = (
        warehouses_df["WarehouseID"]
        .tolist()
    )



    # Avoid duplicate Product + Warehouse pairs

    combinations = []


    for product_id in product_ids:

        for warehouse_id in warehouse_ids:

            combinations.append(
                (
                    product_id,
                    warehouse_id
                )
            )



    # Shuffle combinations

    random.shuffle(
        combinations
    )



    selected_combinations = combinations[
        :NUMBER_OF_INVENTORY_RECORDS
    ]



    inventory_id = 1



    for product_id, warehouse_id in selected_combinations:


        inventory_record = {


            "InventoryID":
                inventory_id,


            "ProductID":
                product_id,


            "WarehouseID":
                warehouse_id,


            "QuantityOnHand":
                generate_quantity(),


            "ReorderLevel":
                random.choice(
                    INVENTORY_REORDER_LEVELS
                )

        }


        inventory.append(
            inventory_record
        )


        inventory_id += 1



    return pd.DataFrame(
        inventory
    )



# ------------------------------------------
# Run generator
# ------------------------------------------

if __name__ == "__main__":


    inventory_df = generate_inventory()


    save_to_csv(
        inventory_df,
        "inventory.csv"
    )


    print(
        "Inventory data generation completed."
    )