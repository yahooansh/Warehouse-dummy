-- =============================================
-- PRIMARY KEYS
-- =============================================
USE WarehouseAnalytics;
GO

ALTER TABLE Warehouses
ADD CONSTRAINT PK_Warehouses
PRIMARY KEY (WarehouseID);
GO


ALTER TABLE Employees
ADD CONSTRAINT PK_Employees
PRIMARY KEY (EmployeeID);
GO


ALTER TABLE Suppliers
ADD CONSTRAINT PK_Suppliers
PRIMARY KEY (SupplierID);
GO


ALTER TABLE Products
ADD CONSTRAINT PK_Products
PRIMARY KEY (ProductID);
GO


ALTER TABLE Inventory
ADD CONSTRAINT PK_Inventory
PRIMARY KEY (InventoryID);
GO


ALTER TABLE Orders
ADD CONSTRAINT PK_Orders
PRIMARY KEY (OrderID);
GO


ALTER TABLE OrderItems
ADD CONSTRAINT PK_OrderItems
PRIMARY KEY (OrderItemID);
GO


ALTER TABLE InventoryAudits
ADD CONSTRAINT PK_InventoryAudits
PRIMARY KEY (AuditID);
GO


ALTER TABLE InventoryDefects
ADD CONSTRAINT PK_InventoryDefects
PRIMARY KEY (DefectID);
GO


ALTER TABLE DailyKPIs
ADD CONSTRAINT PK_DailyKPIs
PRIMARY KEY (KPIID);
GO

-- =============================================
-- FOREIGN KEYS
-- =============================================

                    PARENT TABLES
                             
        Suppliers                 Warehouses
            |                         |
            |                         |
            ↓                         ↓

        Products                 Employees
            |                         |
            |                         |
            ↓                         ↓

 ---------------------------------------------------
 |                     |                           |
 ↓                     ↓                           ↓

Inventory          Orders                 InventoryAudits
 |                   |                           |
 |                   |                           |
 ↓                   ↓                           ↓

Products         OrderItems               InventoryDefects
                     |
                     |
                     ↓
                  Products


Warehouses
     |
     ↓
 DailyKPIs


-- Employees -> Warehouses
ALTER TABLE Employees
ADD CONSTRAINT FK_Employees_Warehouses
FOREIGN KEY (WarehouseID)
REFERENCES Warehouses(WarehouseID);
GO

-- Products -> Suppliers
ALTER TABLE Products
ADD CONSTRAINT FK_Products_Suppliers
FOREIGN KEY (SupplierID)
REFERENCES Suppliers(SupplierID);
GO


-- Inventory -> Warehouses
ALTER TABLE Inventory
ADD CONSTRAINT FK_Inventory_Warehouses
FOREIGN KEY (WarehouseID)
REFERENCES Warehouses(WarehouseID);
GO


-- Inventory -> Products
ALTER TABLE Inventory
ADD CONSTRAINT FK_Inventory_Products
FOREIGN KEY (ProductID)
REFERENCES Products(ProductID);
GO


-- Orders -> Warehouses
ALTER TABLE Orders
ADD CONSTRAINT FK_Orders_Warehouses
FOREIGN KEY (WarehouseID)
REFERENCES Warehouses(WarehouseID);
GO


-- OrderItems -> Orders
ALTER TABLE OrderItems
ADD CONSTRAINT FK_OrderItems_Orders
FOREIGN KEY (OrderID)
REFERENCES Orders(OrderID);
GO


-- OrderItems -> Products
ALTER TABLE OrderItems
ADD CONSTRAINT FK_OrderItems_Products
FOREIGN KEY (ProductID)
REFERENCES Products(ProductID);
GO


-- InventoryAudits -> Warehouses
ALTER TABLE InventoryAudits
ADD CONSTRAINT FK_InventoryAudits_Warehouses
FOREIGN KEY (WarehouseID)
REFERENCES Warehouses(WarehouseID);
GO


-- InventoryAudits -> Employees
ALTER TABLE InventoryAudits
ADD CONSTRAINT FK_InventoryAudits_Employees
FOREIGN KEY (EmployeeID)
REFERENCES Employees(EmployeeID);
GO


-- InventoryAudits -> Products
ALTER TABLE InventoryAudits
ADD CONSTRAINT FK_InventoryAudits_Products
FOREIGN KEY (ProductID)
REFERENCES Products(ProductID);
GO


-- InventoryDefects -> Warehouses
ALTER TABLE InventoryDefects
ADD CONSTRAINT FK_InventoryDefects_Warehouses
FOREIGN KEY (WarehouseID)
REFERENCES Warehouses(WarehouseID);
GO


-- InventoryDefects -> Employees
ALTER TABLE InventoryDefects
ADD CONSTRAINT FK_InventoryDefects_Employees
FOREIGN KEY (EmployeeID)
REFERENCES Employees(EmployeeID);
GO


-- InventoryDefects -> Products
ALTER TABLE InventoryDefects
ADD CONSTRAINT FK_InventoryDefects_Products
FOREIGN KEY (ProductID)
REFERENCES Products(ProductID);
GO


-- DailyKPIs -> Warehouses
ALTER TABLE DailyKPIs
ADD CONSTRAINT FK_DailyKPIs_Warehouses
FOREIGN KEY (WarehouseID)
REFERENCES Warehouses(WarehouseID);
GO

-- =============================================
-- UNIQUE CONSTRAINTS
-- =============================================


-- Warehouse code must be unique
ALTER TABLE Warehouses
ADD CONSTRAINT UQ_Warehouses_WarehouseCode
UNIQUE (WarehouseCode);
GO


-- Supplier email must be unique
ALTER TABLE Suppliers
ADD CONSTRAINT UQ_Suppliers_Email
UNIQUE (Email);
GO


-- Product SKU must be unique
ALTER TABLE Products
ADD CONSTRAINT UQ_Products_SKU
UNIQUE (SKU);
GO

-- =============================================
-- CHECK CONSTRAINTS
-- =============================================


-- Product price cannot be negative
ALTER TABLE Products
ADD CONSTRAINT CK_Products_UnitPrice_Positive
CHECK (UnitPrice >= 0);
GO


-- Inventory quantities cannot be negative
ALTER TABLE Inventory
ADD CONSTRAINT CK_Inventory_Quantity_Positive
CHECK (
    QuantityOnHand >= 0
    AND QuantityReserved >= 0
    AND QuantityDamaged >= 0
);
GO


-- Order status validation
ALTER TABLE Orders
ADD CONSTRAINT CK_Orders_Status
CHECK (
    OrderStatus IN
    ('Pending','Processing','Shipped','Delivered','Cancelled')
);
GO


-- Inventory accuracy must be between 0 and 100
ALTER TABLE DailyKPIs
ADD CONSTRAINT CK_DailyKPIs_Accuracy
CHECK (InventoryAccuracy BETWEEN 0 AND 100);
GO


-- Defect severity validation
ALTER TABLE InventoryDefects
ADD CONSTRAINT CK_InventoryDefects_Severity
CHECK (
    Severity IN ('Low','Medium','High','Critical')
);
GO

-- =============================================
-- DEFAULT CONSTRAINTS
-- =============================================


ALTER TABLE Employees
ADD CONSTRAINT DF_Employees_IsActive
DEFAULT 1 FOR IsActive;
GO


ALTER TABLE Suppliers
ADD CONSTRAINT DF_Suppliers_IsActive
DEFAULT 1 FOR IsActive;
GO


ALTER TABLE Products
ADD CONSTRAINT DF_Products_IsActive
DEFAULT 1 FOR IsActive;
GO


ALTER TABLE InventoryDefects
ADD CONSTRAINT DF_InventoryDefects_Resolved
DEFAULT 0 FOR Resolved;
GO

-- Check unique constraints
USE WarehouseAnalytics;
SELECT * 
FROM sys.objects
WHERE type = 'UQ';
