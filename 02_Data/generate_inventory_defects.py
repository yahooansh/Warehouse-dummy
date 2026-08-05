# ==========================================
# Purpose:
# Generate inventory defect records.
# Connects inventory with employees.
# ==========================================


import random
import pandas as pd


from config import (
    NUMBER_OF_INVENTORY_DEFECTS,
    DEFECT_TYPES
)


from csv_writer import save_to_csv


from data_generator import (
    SEED_VALUE
)



# Make output reproducible

random.seed(SEED_VALUE)



# ------------------------------------------
# Generate inventory defects
# ------------------------------------------

def generate_inventory_defects():


    defects = []


    # Read existing data

    inventory_df = pd.read_csv(
        "../03_Raw_Data/inventory.csv"
    ).dropna()


    employees_df = pd.read_csv(
        "../03_Raw_Data/employees.csv"
    ).dropna()



    inventory_ids = (
        inventory_df["InventoryID"]
        .tolist()
    )


    employee_ids = (
        employees_df["EmployeeID"]
        .tolist()
    )



    for defect_id in range(
        1,
        NUMBER_OF_INVENTORY_DEFECTS + 1
    ):


        defect = {


            "DefectID":
                defect_id,


            "InventoryID":
                random.choice(
                    inventory_ids
                ),


            "EmployeeID":
                random.choice(
                    employee_ids
                ),


            "DefectType":
                random.choice(
                    DEFECT_TYPES
                ),


            "QuantityAffected":
                random.randint(
                    1,
                    20
                ),


            "DefectDate":
                pd.Timestamp(
                    "2026-01-01"
                )
                +
                pd.Timedelta(
                    days=random.randint(
                        0,
                        364
                    )
                )

        }


        defects.append(
            defect
        )



    return pd.DataFrame(
        defects
    )



# ------------------------------------------
# Run generator
# ------------------------------------------

if __name__ == "__main__":


    defects_df = generate_inventory_defects()


    save_to_csv(
        defects_df,
        "inventory_defects.csv"
    )


    print(
        "Inventory defect data generation completed."
    )