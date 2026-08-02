# Warehouse Inventory Analytics Database Design

## Project Overview

This project is about making a dummy warehouse inventory and operations analytics system similar to a large-scale e-commerce fulfillment center.

The purpose of this database is to support:

- Inventory accuracy analysis
- Quality assurance (ICQA) reporting
- Defect investigation
- Operational performance tracking
- Data-driven decision making

## Business Scenario

NorthStar Fulfillment Center manages:

- Multiple warehouses
- Employees
- Suppliers
- Products
- Inventory levels
- Customer orders
- Inventory audits
- Quality defects

## Database Goals

The database should support:

- Accurate inventory tracking
- Root cause analysis of defects
- Operational KPI reporting
- Advanced SQL analytics
- Automated reporting

## Planned Tables

The database will contain the following main tables:

1. Warehouses
2. Employees
3. Suppliers
4. Products
5. Inventory
6. Orders
7. OrderItems
8. InventoryAudits
9. InventoryDefects
10. DailyKPIs

## Design Approach

The database will use:

- Primary keys to uniquely identify records
- Foreign keys to maintain relationships
- Constraints to ensure data integrity
- Indexes to improve query performance
- Stored procedures for automation