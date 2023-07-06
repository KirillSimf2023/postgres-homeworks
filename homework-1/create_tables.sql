-- SQL-команды для создания таблиц


CREATE TABLE employees
(
    employee_id int PRIMARY KEY,
	first_name text NOT NULL,
	last_name text NOT NULL,
	title text,
	birth_date date not null,
	notes text
);

CREATE TABLE customers
(
    customer_id int PRIMARY KEY,
	company_name text NOT NULL,
	contact_name text
);

CREATE TABLE orders
(
    order_id int PRIMARY KEY,
	customer_id int REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date,
	ship_city text
);