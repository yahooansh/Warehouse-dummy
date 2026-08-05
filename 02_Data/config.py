# ==========================================
#  Configuration
# ==========================================

NUMBER_OF_SUPPLIERS = 50
NUMBER_OF_WAREHOUSES = 10
NUMBER_OF_EMPLOYEES = 100
NUMBER_OF_PRODUCTS = 500
NUMBER_OF_ORDERS = 5000
NUMBER_OF_INVENTORY = 5000
NUMBER_OF_ORDER_ITEMS = 15000
NUMBER_OF_AUDITS = 1000
NUMBER_OF_INVENTORY_DEFECTS = 500
NUMBER_OF_KPI_DAYS = 365


# ==========================================
# Warehouse Locations
# ==========================================

WAREHOUSE_CITIES = [
    "Toronto",
    "Mississauga",
    "Brampton",
    "Vaughan",
    "Ottawa",
    "Montreal",
    "Calgary",
    "Edmonton",
    "Vancouver",
    "Halifax"
]

WAREHOUSE_PROVINCES = {
    "Toronto": "Ontario",
    "Mississauga": "Ontario",
    "Brampton": "Ontario",
    "Vaughan": "Ontario",
    "Ottawa": "Ontario",
    "Montreal": "Quebec",
    "Calgary": "Alberta",
    "Edmonton": "Alberta",
    "Vancouver": "British Columbia",
    "Halifax": "Nova Scotia"
}


EMPLOYEE_ROLES = [
    "Warehouse Manager",
    "Inventory Specialist",
    "Forklift Operator",
    "Quality Analyst",
    "Shipping Coordinator",
    "Receiving Clerk"
]

PRODUCT_CATEGORIES = [
    "Electronics",
    "Warehouse Equipment",
    "Safety Equipment",
    "Packaging Material",
    "Office Supplies",
    "Tools",
    "Machinery Parts"
]


NUMBER_OF_INVENTORY_RECORDS = 5000


INVENTORY_REORDER_LEVELS = [
    25,
    50,
    100,
    200
]


ORDER_STATUSES = [
    "Pending",
    "Processing",
    "Shipped",
    "Delivered",
    "Cancelled"
]


AUDIT_RESULTS = [
    "Matched",
    "Shortage",
    "Overage"
]


DEFECT_TYPES = [
    "Damaged",
    "Expired",
    "Missing",
    "Packaging Issue",
    "Quality Failure"
]