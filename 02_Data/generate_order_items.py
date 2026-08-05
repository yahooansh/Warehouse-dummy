# ==========================================
# Purpose:
# Generate order line-item data.
# Connects orders with products.
# ==========================================


import random
import pandas as pd


from config import (
    NUMBER_OF_ORDER_ITEMS
)


from csv_writer import save_to_csv


from data_generator import (
    generate_quantity,
    SEED_VALUE
)



# Make output reproducible

random.seed(SEED_VALUE)



# ------------------------------------------
# Generate order items
# ------------------------------------------

def generate_order_items():


    order_items = []


    # Read existing data

    orders_df = pd.read_csv(
        "../03_Raw_Data/orders.csv"
    )


    products_df = pd.read_csv(
        "../03_Raw_Data/products.csv"
    )



    order_ids = (
        orders_df["OrderID"]
        .tolist()
    )


    product_data = (
        products_df[
            [
                "ProductID",
                "UnitPrice"
            ]
        ]
        .values
        .tolist()
    )



    # Create unique item IDs

    order_item_id = 1



    for i in range(
        NUMBER_OF_ORDER_ITEMS
    ):


        selected_order = random.choice(
            order_ids
        )


        selected_product = random.choice(
            product_data
        )


        product_id = selected_product[0]


        unit_price = selected_product[1]



        order_item = {


            "OrderItemID":
                order_item_id,


            "OrderID":
                selected_order,


            "ProductID":
                product_id,


            "Quantity":
                generate_quantity(),


            "UnitPrice":
                unit_price

        }


        order_items.append(
            order_item
        )


        order_item_id += 1



    return pd.DataFrame(
        order_items
    )



# ------------------------------------------
# Run generator
# ------------------------------------------

if __name__ == "__main__":


    order_items_df = generate_order_items()


    save_to_csv(
        order_items_df,
        "order_items.csv"
    )


    print(
        "Order item data generation completed."
    )