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

