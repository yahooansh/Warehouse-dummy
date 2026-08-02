# Warehouse Inventory Analytics Database - Data Dictionary

## Project Overview

This database simulates a large scale e-commerce fulfillment center analytics system.

The database supports:

- Inventory management
- Inventory accuracy tracking
- Quality assurance (ICQA) audits
- Defect analysis
- Warehouse operations reporting
- SQL analytics and automation


# 1. Warehouses Table

## Purpose

Stores information about fulfillment centers where inventory operations occur.

## Table Name

`Warehouses`

## Columns

| Column Name | Data Type | Constraint | Description |
|-------------|-----------|-------------|-------------|
| WarehouseID | INT | Primary Key | Unique identifier for each warehouse |
| WarehouseCode | VARCHAR(10) | Unique, Not Null | Short code for warehouse |
| WarehouseName | VARCHAR(100) | Not Null | Warehouse name |
| City | VARCHAR(50) | Not Null | City location |
| Province | VARCHAR(50) | Not Null | Province/state |
| Country | VARCHAR(50) | Not Null | Country |
| Capacity | INT | Not Null | Maximum storage capacity |
| CreatedDate | DATE | Not Null | Date warehouse was added |


## Relationships

One warehouse can have:

- Many employees
- Many inventory records
- Many orders
- Many audits


---

# 2. Employees Table

## Purpose

Stores warehouse employee information.

## Table Name

`Employees`

## Columns

| Column Name | Data Type | Constraint | Description |
|-------------|-----------|-------------|-------------|
| EmployeeID | INT | Primary Key | Unique employee identifier |
| WarehouseID | INT | Foreign Key | Assigned warehouse |
| FirstName | VARCHAR(50) | Not Null | Employee first name |
| LastName | VARCHAR(50) | Not Null | Employee last name |
| JobTitle | VARCHAR(50) | Not Null | Employee role |
| Department | VARCHAR(50) | Not Null | Department name |
| HireDate | DATE | Not Null | Employee joining date |
| Shift | VARCHAR(20) | Not Null | Work shift |
| IsActive | BIT | Not Null | Employment status |


## Relationships

Many employees belong to one warehouse.


Relationship:


Warehouses
|
|
Employees



---

# 3. Suppliers Table

## Purpose

Stores supplier information for products received into the warehouse.

## Table Name

`Suppliers`

## Columns

| Column Name | Data Type | Constraint | Description |
|-------------|-----------|-------------|-------------|
| SupplierID | INT | Primary Key | Unique supplier identifier |
| SupplierName | VARCHAR(100) | Not Null | Supplier company name |
| ContactName | VARCHAR(100) | Null | Supplier contact person |
| Email | VARCHAR(100) | Unique | Supplier email |
| PhoneNumber | VARCHAR(20) | Null | Contact number |
| Country | VARCHAR(50) | Not Null | Supplier country |
| SupplierRating | DECIMAL(3,2) | Null | Quality rating |
| CreatedDate | DATE | Not Null | Supplier registration date |


## Relationships

One supplier can provide many products.


Relationship:


Suppliers
|
|
Products



---

# 4. Products Table

## Purpose

Stores information about products handled by the fulfillment center.

## Table Name

`Products`

## Columns

| Column Name | Data Type | Constraint | Description |
|-------------|-----------|-------------|-------------|
| ProductID | INT | Primary Key | Unique product identifier |
| SupplierID | INT | Foreign Key | Product supplier |
| SKU | VARCHAR(50) | Unique, Not Null | Stock keeping unit |
| ProductName | VARCHAR(100) | Not Null | Product description |
| Category | VARCHAR(50) | Not Null | Product category |
| UnitCost | DECIMAL(10,2) | Not Null | Product cost |
| WeightKG | DECIMAL(8,2) | Null | Product weight |
| IsActive | BIT | Not Null | Product availability |
| CreatedDate | DATE | Not Null | Product creation date |


## Relationships

Many products belong to one supplier.


Relationship:


Suppliers
|
|
Products



---

# 5. Inventory Table

## Purpose

Tracks current inventory quantities stored inside warehouses.

## Table Name

`Inventory`

## Columns

| Column Name | Data Type | Constraint | Description |
|-------------|-----------|-------------|-------------|
| InventoryID | INT | Primary Key | Inventory record ID |
| WarehouseID | INT | Foreign Key | Warehouse location |
| ProductID | INT | Foreign Key | Stored product |
| StorageLocation | VARCHAR(50) | Not Null | Bin/shelf location |
| QuantityOnHand | INT | Not Null | Current quantity |
| LastUpdated | DATETIME | Not Null | Last inventory update |


## Relationships


Warehouse
|
Inventory
|
Product



---

# 6. Inventory Audits Table

## Purpose

Stores ICQA inventory verification records.

## Table Name

`InventoryAudits`

## Columns

| Column Name | Data Type | Constraint | Description |
|-------------|-----------|-------------|-------------|
| AuditID | INT | Primary Key | Audit identifier |
| EmployeeID | INT | Foreign Key | Employee performing audit |
| ProductID | INT | Foreign Key | Audited product |
| WarehouseID | INT | Foreign Key | Audit location |
| AuditDate | DATETIME | Not Null | Audit timestamp |
| ExpectedQuantity | INT | Not Null | System quantity |
| CountedQuantity | INT | Not Null | Physical count |
| AuditStatus | VARCHAR(20) | Not Null | Pass/Fail status |


---

# 7. Inventory Defects Table

## Purpose

Stores inventory accuracy issues identified during audits.

## Table Name

`InventoryDefects`

## Columns

| Column Name | Data Type | Constraint | Description |
|-------------|-----------|-------------|-------------|
| DefectID | INT | Primary Key | Defect identifier |
| AuditID | INT | Foreign Key | Related audit |
| DefectType | VARCHAR(50) | Not Null | Defect category |
| DefectQuantity | INT | Not Null | Quantity difference |
| RootCause | VARCHAR(200) | Null | Cause analysis |
| ResolutionStatus | VARCHAR(30) | Not Null | Resolution state |
| CreatedDate | DATE | Not Null | Defect creation date |


---

# Future Tables

Additional tables will be added:

- Orders
- OrderItems
- Shipments
- DailyKPIs
- EmployeePerformance

# 8. Orders Table

## Purpose

Stores customer order information. This table represents outbound fulfillment activity where customers place orders and products are picked, packed, and shipped.

## Table Name

`Orders`

## Columns

| Column Name | Data Type | Constraint | Description |
|-------------|-----------|-------------|-------------|
| OrderID | INT | Primary Key | Unique customer order identifier |
| WarehouseID | INT | Foreign Key | Warehouse fulfilling the order |
| OrderDate | DATETIME | Not Null | Date and time order was created |
| CustomerID | VARCHAR(50) | Not Null | Customer identifier |
| OrderStatus | VARCHAR(30) | Not Null | Current order status |
| Priority | VARCHAR(20) | Not Null | Order priority level |
| ShipDate | DATETIME | Null | Date order was shipped |
| TotalOrderValue | DECIMAL(12,2) | Not Null | Total monetary value of order |
| CreatedDate | DATETIME | Not Null | Record creation timestamp |

## Relationships

One warehouse can fulfill many orders.

One order can contain many order items.

Relationship:


Warehouses
|
|
Orders
|
|
OrderItems


---

# 9. OrderItems Table

## Purpose

Stores individual products included in customer orders.

An order may contain multiple products, therefore this table acts as a transaction detail table.

## Table Name

`OrderItems`

## Columns

| Column Name | Data Type | Constraint | Description |
|-------------|-----------|-------------|-------------|
| OrderItemID | INT | Primary Key | Unique order item identifier |
| OrderID | INT | Foreign Key | Related customer order |
| ProductID | INT | Foreign Key | Ordered product |
| QuantityOrdered | INT | Not Null | Quantity requested |
| UnitPrice | DECIMAL(10,2) | Not Null | Selling price per unit |
| FulfillmentStatus | VARCHAR(30) | Not Null | Pick/pack/shipped status |
| CreatedDate | DATETIME | Not Null | Record creation timestamp |

## Relationships

One order has many order items.

One product can appear in many order items.

Relationship:


Orders
|
|
OrderItems
|
|
Products


---

# 10. DailyKPIs Table

## Purpose

Stores daily warehouse performance metrics.

This table supports operational reporting and dashboard creation.

Examples:

- Inventory accuracy %
- Order fulfillment rate
- Defect rate
- Productivity metrics

## Table Name

`DailyKPIs`

## Columns

| Column Name | Data Type | Constraint | Description |
|-------------|-----------|-------------|-------------|
| KPIID | INT | Primary Key | KPI record identifier |
| WarehouseID | INT | Foreign Key | Warehouse being measured |
| KPI_Date | DATE | Not Null | Date of measurement |
| InventoryAccuracy | DECIMAL(5,2) | Not Null | Inventory accuracy percentage |
| TotalOrders | INT | Not Null | Number of orders processed |
| OrdersCompleted | INT | Not Null | Successfully completed orders |
| TotalDefects | INT | Not Null | Number of defects identified |
| DefectRate | DECIMAL(5,2) | Not Null | Defects percentage |
| AverageProcessingTime | DECIMAL(10,2) | Null | Average order processing time |
| CreatedDate | DATETIME | Not Null | Record creation timestamp |

## Relationships

One warehouse has many daily KPI records.

Relationship:


Warehouses
|
|
DailyKPIs


---

# Complete Database Table List

The final database will contain:

| Table | Purpose |
|------|---------|
| Warehouses | Stores fulfillment center information |
| Employees | Stores warehouse employee information |
| Suppliers | Stores product suppliers |
| Products | Stores product catalog |
| Inventory | Tracks inventory levels |
| Orders | Stores customer orders |
| OrderItems | Stores products within orders |
| InventoryAudits | Stores ICQA audit records |
| InventoryDefects | Stores inventory accuracy issues |
| DailyKPIs | Stores operational performance metrics |


# Final database relationship model
                    Suppliers
                        |
                        |
                    Products
                        |
          -----------------------------
          |                           |
      Inventory                  OrderItems
          |                           |
          |                           |
     Warehouses ---------------- Orders
          |
          |
    Employees

          |
          |
 InventoryAudits
          |
          |
 InventoryDefects


          |
          |
      DailyKPIs