-- Create the PRODUCTS table if it does not exist
CREATE TABLE IF NOT EXIST PRODUCTS (
    PRODUCT_ID TEXT,
    PRODUCT_NAME,
    SUPPLIER_TEXT,
    CATEGORY_ID TEXT,
    UNIT_TEXT,
    PRICE_REAL
);

-- Insert sample data into the PRODUCTS table 
INSERT INTO PRODUCTS (PRODUCTS_ID, PRODUCT_NAME, SUPPLIER_ID, CATEGORY_ID, UNIT_TEXT, PRICE_REAL) VALUES
('1', 'CHAIS', '1', '1', '10 BOXES*20 BAGS', 18),
('2', 'CHANG', '1', '1', '24-12 OZ BOTTLES', 10),
('3', 'ANISEED SYRUP', '1', '2', '12-550 ML BOTTLES', 10),
('4', 'CHEF ANTON SEASONING', '2', '2', '48-5 OZ JARS', 22), 
('5', 'CHEF ANTON MIX', '2', '2', '36 BOXES', 21.35);
 
-- Query to count the number of products
SELECT COUNT (PRODUCTS_ID) As Product_Count
FROM PRODUCTS;

-- Query to find the averge price of products 
SELECT AVG(PRICE) AS Average_Price
FROM PRODUCTS;

-- QUery to find the total price of products
SELECT SUM(PRICE) AS Total_Price
FROM PRODUCTS;