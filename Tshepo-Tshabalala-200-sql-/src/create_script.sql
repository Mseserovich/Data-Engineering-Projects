DROP TABLE IF EXISTS
    Customers,
    Products,
    Payments,
    Employees,
    Orders
    CASCADE;

CREATE TABLE Customers(
    Id SERIAL,
    FIRSTNAME VARCHAR(50),
    LASTNAME VARCHAR(50),
    GENDER VARCHAR,
    ADDRESS VARCHAR(200),
    PHONE BIGINT,
    EMAIL VARCHAR(100),
    CITY VARCHAR(20),
    COUNTRY VARCHAR(50),
    PRIMARY KEY (Id)
);

CREATE TABLE Products (
    Id SERIAL,
    ProductName varchar(100),
    Description varchar(300),
    BuyPrice decimal,
    PRIMARY KEY (Id)
);

CREATE TABLE Payments (
    CustomerId int,
    Id SERIAL,
    PaymentDate date,
    Amount decimal,
    PRIMARY KEY (Id),
    FOREIGN KEY (CustomerId) REFERENCES Customers (Id)

);

CREATE TABLE Employees (
    Id SERIAL,
    FirstName varchar(50),
    LastName varchar(50),
    Email varchar(100),
    JobTitle varchar(20),
    PRIMARY KEY (Id)
);

CREATE TABLE Orders (
    Id SERIAL,
    ProductID int,
    PaymentID int,
    FullfilledByEmployeeID int,
    DateRequired date,
    DateShipped date,
    Status varchar(20),
    PRIMARY KEY (Id),
    FOREIGN KEY (ProductID) REFERENCES Products (Id),
    FOREIGN KEY (PaymentID) REFERENCES Payments (Id),
    FOREIGN KEY (FullfilledByEmployeeID) REFERENCES Employees (Id)
);

INSERT INTO customers (FIRSTNAME, LASTNAME, GENDER, ADDRESS, PHONE, EMAIL, CITY, COUNTRY)
VALUES  ('John', 'Hilbert', 'Male', '284 chaucer st', 084789657, 'John@gmail.com', 'Johannesburg', 'South Africa'),
        ('Thando', 'Sithole', 'Female', '240 Sect 1', 0794445584, 'Thando@gmail.com', 'Capetown', 'South Africa'),
        ('Leon', 'Glen', 'Male', '81 Everton Rd,Gillits', 0820832830, 'Leon@gmail.com', 'Durban', 'South Africa'),
        ('Charl', 'Muller', 'Mal', '290A Dorset Ecke', +44856872553, 'Charl.muller@yahoo.com', 'Berlin', 'Germany'),
        ('Julia', 'Stein', 'Female', '2 Wernerring', +448672445058, 'Js234@yahoo.com', 'Frankfurt', 'Germany');

INSERT INTO Employees (FirstName, LastName, Email, JobTitle)
VALUES  ('Kani', 'Matthew', 'Mat@gmail.com', 'Manager'),
        ('Lesly', 'Cronje', 'lesC@gmail.com', 'Clerk'),
        ('Gideon', 'Maduku', 'm@gmail.com', 'Accountant');

INSERT INTO Products (ProductName, Description, BuyPrice)
VALUES  ('Harley Davidson Chopper', 'This replica features working kickstand, front suspension, gear-shift lever', 150.75),
        ('Classic Car', 'Turnable front wheels, steering function', 550.75),
        ('Sports Car', 'Turnable front wheels, steering function', 700.60);

INSERT INTO payments (CustomerId, PaymentDate, Amount)
VALUES  (1, '01-09-2018', 150.75),
        (5, '03-09-2018', 150.75),
        (4, '03-09-2018', 700.60);

INSERT INTO Orders (ProductID, PaymentID, FullfilledByEmployeeID, DateRequired, Status)
VALUES  (1,1,2, '05-09-2018', 'Not Shipped');

INSERT INTO Orders (ProductID, PaymentID, FullfilledByEmployeeID, DateRequired, DateShipped, Status)
VALUES  (1,1,2, '05-09-2018', '03-09-2018', 'Shipped');

INSERT INTO Orders (ProductID, PaymentID, FullfilledByEmployeeID, DateRequired, Status)
VALUES  (3,3,3, '06-09-2018', 'Not Shipped');

SELECT * FROM Customers;

SELECT firstname, lastname FROM Customers;

SELECT firstname, lastname FROM Customers
WHERE Id = 1;

UPDATE Customers
SET firstname = 'Lerato', lastname = 'Mabitso'
WHERE Id = 1;

DELETE FROM Customers WHERE Id = 2;

SELECT DISTINCT(Status), Count(DISTINCT(Status))
FROM Orders
Group By Status;

SELECT MAX(amount) AS Highest_Amount FROM Payments;

SELECT * FROM Customers
Order by Country;

SELECT * FROM Products
WHERE BuyPrice BETWEEN 100 AND 600;

SELECT * FROM Customers
WHERE Country = 'Germany'
AND City = 'Berlin';

SELECT * FROM Customers
WHERE City = 'Durban' OR City = 'Capetown';

SELECT * FROM Products
WHERE BuyPrice > 500;

SELECT SUM(amount) AS "total amount" From Payments;

SELECT Status , Count(Status) FROM Orders
WHERE Status = 'Shipped'
Group By Status;

SELECT ROUND(AVG(BuyPrice), 2) AS "Rands", ROUND(AVG(BuyPrice * 12), 2) AS "Dollars"
FROM Products;

SELECT Payments.*, Customers.* FROM Payments
INNER JOIN Customers
ON Payments.CustomerId = Customers.Id;

SELECT * FROM Products
WHERE lower(description) LIKE '%turnable front wheels%';




