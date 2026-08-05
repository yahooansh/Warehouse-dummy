# ==========================================
# Purpose:
# Generate employee master data.
# Employees are assigned to existing warehouses.
# ==========================================


import random
import pandas as pd


from config import (
    NUMBER_OF_EMPLOYEES,
    EMPLOYEE_ROLES
)


from csv_writer import save_to_csv


from data_generator import (
    fake,
    generate_status,
    SEED_VALUE
)



# Make random selection reproducible

random.seed(SEED_VALUE)



# ------------------------------------------
# Generate employees
# ------------------------------------------

def generate_employees():


    employees = []


    # Read warehouse data

    warehouses_df = pd.read_csv(
        "../03_Raw_Data/warehouses.csv"
    )


    warehouse_ids = (
        warehouses_df["WarehouseID"]
        .tolist()
    )



    for employee_id in range(
        1,
        NUMBER_OF_EMPLOYEES + 1
    ):


        first_name = fake.first_name()

        last_name = fake.last_name()



        employee = {


            "EmployeeID": employee_id,


            "FirstName": first_name,


            "LastName": last_name,


            "Email":

                f"{first_name.lower()}."
                f"{last_name.lower()}@example.com",


            "PhoneNumber":

                fake.phone_number(),


            "Role":

                random.choice(
                    EMPLOYEE_ROLES
                ),


            "WarehouseID":

                random.choice(
                    warehouse_ids
                ),


            "IsActive":

                generate_status()

        }


        employees.append(
            employee
        )


    return pd.DataFrame(
        employees
    )



# ------------------------------------------
# Run generator
# ------------------------------------------

if __name__ == "__main__":


    employees_df = generate_employees()


    save_to_csv(
        employees_df,
        "employees.csv"
    )


    print(
        "Employee data generation completed."
    )