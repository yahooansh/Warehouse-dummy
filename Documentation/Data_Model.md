# Warehouse Analytics - Data Generation Model

## Purpose

This document describes how synthetic data is generated for the Warehouse Analytics project.

The objective is to create realistic operational warehouse data that supports advanced SQL analysis, reporting, and automation.

---

## Data Volume

| Table | Records |
|--------|--------:|
| Suppliers | 50 |
| Warehouses | 10 |
| Employees | 100 |
| Products | 500 |
| Inventory | 5,000 |
| Orders | 5,000 |
| OrderItems | 15,000 |
| InventoryAudits | 1,000 |
| InventoryDefects | 500 |
| DailyKPIs | 3,650 |

---

## Relationship Rules

- Every Product belongs to exactly one Supplier.
- Every Employee belongs to exactly one Warehouse.
- Every Inventory record belongs to one Warehouse and one Product.
- Every Order is processed by one Warehouse.
- Every OrderItem belongs to one Order and one Product.
- Every InventoryAudit is performed by one Employee on one Product in one Warehouse.
- Every InventoryDefect belongs to one Product, one Warehouse, and one Employee.
- Every DailyKPI belongs to one Warehouse for one calendar day.