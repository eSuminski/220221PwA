# SQL Practice
There is a high chance you will be asked to write a SQL query. The chinook database is a practice database. Run the script here in your DB to get it.
https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_PostgreSql.sql
- Querying practice
    - Select all records from the Employee table.
    - Select all records from the Employee table where last name is King.
    - Select all records from the Employee table where first name is Andrew and REPORTSTO is NULL.
    -  Select all albums in Album table and sort result set in descending order by title.
    - Select first name from Customer and sort result set in ascending order by city
    - Select all invoices with a billing address like “T%”
    - Select all invoices that have a total between 15 and 50
    - Select all employees hired between 1st of June 2003 and 1st of March 2004
- Insert practice
    - Insert two new records into Genre table
    - Insert two new records into Employee table
    - Insert two new records into Customer table
- Update Practice
    - Update Aaron Mitchell in Customer table to Robert Walter
    - Update name of artist in the Artist table “Creedence Clearwater Revival” to “CCR”
- Joins
    - Create an inner join that joins customers and orders and specifies the name of the customer and the invoiceId
    - Create an outer join that joins the customer and invoice table, specifying the CustomerId, firstname, lastname, invoiceId, and total.
    - Create a right join that joins album and artist specifying artist name and title.
    - Create a cross join that joins album and artist and sorts by artist name in ascending order.
    - Perform a self-join on the employee table, joining on the reportsto column.
- Set Operators
    - Use a unionall to create a table that has the name of all employees and customers
