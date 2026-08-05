# ==========================================
# Purpose:
# Generate warehouse master data.
# ==========================================


import random
import pandas as pd



from config import (

    NUMBER_OF_WAREHOUSES,

    WAREHOUSE_CITIES,

    WAREHOUSE_PROVINCES

)



from csv_writer import save_to_csv



from data_generator import (

    generate_warehouse_code,

    generate_status,

    SEED_VALUE

)



# Make random values reproducible

random.seed(SEED_VALUE)




def generate_warehouses():


    warehouses = []


    selected_cities = random.sample(

        WAREHOUSE_CITIES,

        NUMBER_OF_WAREHOUSES

    )



    for warehouse_id, city in enumerate(

        selected_cities,

        start=1

    ):


        warehouse = {


            "WarehouseID": warehouse_id,


            "WarehouseCode": generate_warehouse_code(

                warehouse_id

            ),


            "WarehouseName":

                f"{city} Fulfillment Center",


            "City": city,


            "Province":

                WAREHOUSE_PROVINCES[city],


            "Capacity":

                random.randint(

                    50000,

                    250000

                ),


            "IsActive":

                generate_status()


        }


        warehouses.append(

            warehouse

        )


    return pd.DataFrame(

        warehouses

    )




if __name__ == "__main__":


    warehouses_df = generate_warehouses()



    save_to_csv(

        warehouses_df,

        "warehouses.csv"

    )



    print(

        "Warehouse data generation completed."

    )