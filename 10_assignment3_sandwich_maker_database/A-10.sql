-- Create database
CREATE DATABASE sandwich_maker;

-- Use the database
USE sandwich_maker;

-- Create resources table
CREATE TABLE resources (
    item VARCHAR(50),
    amount INT
);

-- Create sandwiches table
CREATE TABLE sandwiches (
    sandwich_size VARCHAR(50),
    price DECIMAL(5,2)
);

-- Create recipes table
CREATE TABLE recipes (
    sandwich_size VARCHAR(50),
    item VARCHAR(50),
    amount INT
);

-- Insert data into resources
INSERT INTO resources (item, amount) VALUES
('bread', 12),
('ham', 18),
('cheese', 24);

-- Insert data into sandwiches
INSERT INTO sandwiches (sandwich_size, price) VALUES
('small', 1.75),
('medium', 3.25),
('large', 5.50);

-- Insert data into recipes
INSERT INTO recipes (sandwich_size, item, amount) VALUES
('small', 'bread', 2),
('small', 'ham', 4),
('small', 'cheese', 4),
('medium', 'bread', 4),
('medium', 'ham', 6),
('medium', 'cheese', 8),
('large', 'bread', 6),
('large', 'ham', 8),
('large', 'cheese', 12);

-- Select all data from resources
SELECT * FROM resources;

-- Select all data from sandwiches
SELECT * FROM sandwiches;

-- Select all data from recipes
SELECT * FROM recipes;
