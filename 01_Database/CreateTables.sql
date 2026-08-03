USE WarehouseAnalytics;
CREATE TABLE Warehouses
(
    WarehouseID INT IDENTITY(1,1) NOT NULL,
    WarehouseCode VARCHAR(10) NOT NULL,
    WarehouseName VARCHAR(100) NOT NULL,
    City VARCHAR(50) NOT NULL,
    Province VARCHAR(50) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    Capacity INT NOT NULL,
    CreatedDate DATE NOT NULL
);
GO

CREATE TABLE Employees
(
    EmployeeID INT IDENTITY(1,1) NOT NULL,
    WarehouseID INT NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    JobTitle VARCHAR(50) NOT NULL,
    Department VARCHAR(50) NOT NULL,
    HireDate DATE NOT NULL,
    Shift VARCHAR(20) NOT NULL,
    IsActive BIT NOT NULL
);
GO

CREATE TABLE Suppliers
(
    SupplierID INT IDENTITY(1,1) NOT NULL,
    SupplierName VARCHAR(100) NOT NULL,
    ContactName VARCHAR(100) NOT NULL,
    Phone VARCHAR(20) NULL,
    Email VARCHAR(100) NOT NULL,
    City VARCHAR(50) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    IsActive BIT NOT NULL,
    CreatedDate DATE NOT NULL
);
GO

CREATE TABLE Products
(
    ProductID INT IDENTITY(1,1) NOT NULL,
    SupplierID INT NOT NULL,
    SKU VARCHAR(50) NOT NULL,
    ProductName VARCHAR(150) NOT NULL,
    Category VARCHAR(50) NOT NULL,
    UnitPrice DECIMAL(10,2) NOT NULL,
    Weight DECIMAL(10,2) NOT NULL,
    IsActive BIT NOT NULL,
    CreatedDate DATE NOT NULL
);
GO

CREATE TABLE Inventory
(
    InventoryID INT IDENTITY(1,1) NOT NULL,
    WarehouseID INT NOT NULL,
    ProductID INT NOT NULL,
    QuantityOnHand INT NOT NULL,
    QuantityReserved INT NOT NULL,
    QuantityDamaged INT NOT NULL,
    LastUpdated DATETIME NOT NULL
);
GO

CREATE TABLE Orders
(
    OrderID INT IDENTITY(1,1) NOT NULL,
    WarehouseID INT NOT NULL,
    OrderDate DATETIME NOT NULL,
    CustomerID VARCHAR(50) NOT NULL,
    OrderStatus VARCHAR(30) NOT NULL,
    Priority VARCHAR(20) NOT NULL,
    ShippedDate DATETIME NULL
);
GO

CREATE TABLE OrderItems
(
    OrderItemID INT IDENTITY(1,1) NOT NULL,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    QuantityOrdered INT NOT NULL,
    UnitPrice DECIMAL(10,2) NOT NULL
);
GO

CREATE TABLE InventoryAudits
(
    AuditID INT IDENTITY(1,1) NOT NULL,
    WarehouseID INT NOT NULL,
    EmployeeID INT NOT NULL,
    ProductID INT NOT NULL,
    AuditDate DATETIME NOT NULL,
    SystemQuantity INT NOT NULL,
    CountedQuantity INT NOT NULL,
    Variance INT NOT NULL,
    AuditStatus VARCHAR(30) NOT NULL
);
GO

CREATE TABLE InventoryDefects
(
    DefectID INT IDENTITY(1,1) NOT NULL,
    WarehouseID INT NOT NULL,
    ProductID INT NOT NULL,
    EmployeeID INT NOT NULL,
    DefectDate DATETIME NOT NULL,
    DefectType VARCHAR(50) NOT NULL,
    DefectDescription VARCHAR(255) NULL,
    Severity VARCHAR(20) NOT NULL,
    Resolved BIT NOT NULL
);
GO

CREATE TABLE DailyKPIs
(
    KPIID INT IDENTITY(1,1) NOT NULL,
    WarehouseID INT NOT NULL,
    KPI_Date DATE NOT NULL,
    TotalUnitsProcessed INT NOT NULL,
    InventoryAccuracy DECIMAL(5,2) NOT NULL,
    TotalDefects INT NOT NULL,
    OrderAccuracy DECIMAL(5,2) NOT NULL,
    EmployeeProductivity DECIMAL(10,2) NOT NULL
); 
GO 