# ==========================================
# Purpose:
# Generate inventory audit records.
# Connects inventory with employees.
# ==========================================


import random
import pandas as pd


from config import (
    NUMBER_OF_AUDITS,
    AUDIT_RESULTS
)


from csv_writer import save_to_csv


from data_generator import (
    SEED_VALUE
)



# Make random output reproducible

random.seed(SEED_VALUE)



# ------------------------------------------
# Generate inventory audits
# ------------------------------------------

def generate_inventory_audits():


    audits = []


    # Read existing data

    inventory_df = pd.read_csv(
        "../03_Raw_Data/inventory.csv"
    )


    employees_df = pd.read_csv(
        "../03_Raw_Data/employees.csv"
    )



    inventory_records = (
        inventory_df[
            [
                "InventoryID",
                "QuantityOnHand"
            ]
        ]
        .values
        .tolist()
    )


    employee_ids = (
        employees_df["EmployeeID"]
        .tolist()
    )



    for audit_id in range(
        1,
        NUMBER_OF_AUDITS
    ):


        selected_inventory = random.choice(
            inventory_records
        )


        inventory_id = selected_inventory[0]


        system_quantity = selected_inventory[1]



        # Simulate physical count difference

        counted_quantity = max(
            0,
            system_quantity +
            random.randint(
                -10,
                10
            )
        )



        if counted_quantity == system_quantity:

            result = "Matched"

        elif counted_quantity < system_quantity:

            result = "Shortage"

        else:

            result = "Overage"



        audit = {


            "AuditID":
                audit_id,


            "InventoryID":
                inventory_id,


            "EmployeeID":
                random.choice(
                    employee_ids
                ),


            "SystemQuantity":
                system_quantity,


            "CountedQuantity":
                counted_quantity,


            "AuditResult":
                result,


            "AuditDate":
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


        audits.append(
            audit
        )



    return pd.DataFrame(
        audits
    )



# ------------------------------------------
# Run generator
# ------------------------------------------

if __name__ == "__main__":


    audits_df = generate_inventory_audits()


    save_to_csv(
        audits_df,
        "inventory_audits.csv"
    )


    print(
        "Inventory audit data generation completed."
    )