# ==========================================
# Purpose:
# Generate order transaction data.
# Orders are assigned to existing warehouses.
# ==========================================


import random
import pandas as pd


from config import (
    NUMBER_OF_ORDERS,
    ORDER_STATUSES
)


from csv_writer import save_to_csv


from data_generator import (
    SEED_VALUE
)



# For reproducible data

random.seed(SEED_VALUE)



# ------------------------------------------
# Generate orders
# ------------------------------------------

def generate_orders():


    orders = []


    # Read warehouse data

    warehouses_df = pd.read_csv(
        "../03_Raw_Data/warehouses.csv"
    )


    warehouse_ids = (
        warehouses_df["WarehouseID"]
        .tolist()
    )



    for order_id in range(
        1,
        NUMBER_OF_ORDERS + 1
    ):


        order = {


            "OrderID":
                order_id,


            "WarehouseID":
                random.choice(
                    warehouse_ids
                ),


            "OrderDate":
                pd.Timestamp(
                    "2026-01-01"
                )
                +
                pd.Timedelta(
                    days=random.randint(
                        0,
                        364
                    )
                ),


            "OrderStatus":
                random.choice(
                    ORDER_STATUSES
                )

        }


        orders.append(
            order
        )



    return pd.DataFrame(
        orders
    )



# ------------------------------------------
# Run generator
# ------------------------------------------

if __name__ == "__main__":


    orders_df = generate_orders()


    save_to_csv(
        orders_df,
        "orders.csv"
    )


    print(
        "Order data generation completed."
    )