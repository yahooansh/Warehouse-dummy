# ==========================================
# generate_daily_kpis.py
#
# Purpose:
# Create daily warehouse KPIs from
# operational data.
# ==========================================


import pandas as pd


from csv_writer import save_to_csv



# ------------------------------------------
# Generate Daily KPIs
# ------------------------------------------

def generate_daily_kpis():


    # ------------------------------
    # Read operational data
    # ------------------------------

    orders_df = pd.read_csv(
        "../03_Raw_Data/orders.csv"
    )


    order_items_df = pd.read_csv(
        "../03_Raw_Data/order_items.csv"
    )


    audits_df = pd.read_csv(
        "../03_Raw_Data/inventory_audits.csv"
    )


    defects_df = pd.read_csv(
        "../03_Raw_Data/inventory_defects.csv"
    )



    # ------------------------------
    # Convert dates
    # ------------------------------

    orders_df["OrderDate"] = pd.to_datetime(
        orders_df["OrderDate"]
    )


    audits_df["AuditDate"] = pd.to_datetime(
        audits_df["AuditDate"]
    )


    defects_df["DefectDate"] = pd.to_datetime(
        defects_df["DefectDate"]
    )



    # ------------------------------
    # Orders KPI
    # ------------------------------

    daily_orders = (
        orders_df
        .groupby(
            orders_df["OrderDate"].dt.date
        )
        .agg(
            TotalOrders=("OrderID", "count")
        )
        .reset_index()
    )


    daily_orders.rename(
        columns={
            "OrderDate": "KPI_Date"
        },
        inplace=True
    )



    # ------------------------------
    # Sales KPI
    # ------------------------------

    order_items_df["Revenue"] = (
        order_items_df["Quantity"]
        *
        order_items_df["UnitPrice"]
    )


    sales_df = (
        order_items_df
        .merge(
            orders_df[
                [
                    "OrderID",
                    "OrderDate"
                ]
            ],
            on="OrderID"
        )
    )


    daily_sales = (
        sales_df
        .groupby(
            sales_df["OrderDate"].dt.date
        )
        .agg(
            TotalUnitsSold=
                ("Quantity", "sum"),

            TotalRevenue=
                ("Revenue", "sum")
        )
        .reset_index()
    )


    daily_sales.rename(
        columns={
            "OrderDate": "KPI_Date"
        },
        inplace=True
    )



    # ------------------------------
    # Inventory Defect KPI
    # ------------------------------

    daily_defects = (
        defects_df
        .groupby(
            defects_df["DefectDate"].dt.date
        )
        .agg(
            TotalDefects=
                ("QuantityAffected", "sum")
        )
        .reset_index()
    )


    daily_defects.rename(
        columns={
            "DefectDate": "KPI_Date"
        },
        inplace=True
    )



    # ------------------------------
    # Audit Accuracy KPI
    # ------------------------------

    audits_df["IsAccurate"] = (
        audits_df["AuditResult"]
        ==
        "Matched"
    )


    daily_accuracy = (
        audits_df
        .groupby(
            audits_df["AuditDate"].dt.date
        )
        .agg(
            TotalAudits=
                ("AuditID", "count"),

            AccurateAudits=
                ("IsAccurate", "sum")
        )
        .reset_index()
    )


    daily_accuracy["InventoryAccuracy"] = (

        daily_accuracy["AccurateAudits"]

        /

        daily_accuracy["TotalAudits"]

        *

        100
    )


    daily_accuracy.rename(
        columns={
            "AuditDate": "KPI_Date"
        },
        inplace=True
    )



    # ------------------------------
    # Combine all KPIs
    # ------------------------------

    kpi_df = (
        daily_orders

        .merge(
            daily_sales,
            on="KPI_Date",
            how="outer"
        )

        .merge(
            daily_defects,
            on="KPI_Date",
            how="outer"
        )

        .merge(
            daily_accuracy[
                [
                    "KPI_Date",
                    "InventoryAccuracy"
                ]
            ],
            on="KPI_Date",
            how="outer"
        )
    )



    # Fill missing values

    kpi_df.fillna(
        0,
        inplace=True
    )



    # Sort by date

    kpi_df.sort_values(
        "KPI_Date",
        inplace=True
    )



    # Add KPI ID

    kpi_df.insert(
        0,
        "KPI_ID",
        range(
            1,
            len(kpi_df) + 1
        )
    )



    return kpi_df



# ------------------------------------------
# Run
# ------------------------------------------

if __name__ == "__main__":


    kpi_df = generate_daily_kpis()


    save_to_csv(
        kpi_df,
        "daily_kpis.csv"
    )


    print(
        "Daily KPI calculation completed."
    )