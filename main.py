import sqlite3

conn = sqlite3.connect('practice_data.sqlite')

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employeeNumber INTEGER PRIMARY KEY AUTOINCREMENT,
    lastName TEXT NOT NULL,
    firstName TEXT,
    jobTitle TEXT

    );""")

cur.execute("""
CREATE TABLE IF NOT EXISTS orderDetails (
    orderNumber INTEGER PRIMARY KEY AUTOINCREMENT,
    priceEach REAL,
    quantityOrdered INTEGER,
    orderDate TEXT

    );""")

cur.execute("DELETE FROM employees")
cur.execute("DELETE FROM orderDetails")

cur.execute('''
INSERT INTO employees (lastName, firstName, jobTitle) VALUES
            ('Murphy', 'Diane', 'President'),
            ('Patterson', 'Mary', 'VP Sales'),
            ('Firrelli', 'Jeff', 'VP Marketing'),
            ('Bow', 'Anthony', 'Sales Manager (NA)'),
            ('Jennings', 'Leslie', 'Sales Rep'),
            ('Thompson', 'Leslie', 'Sales Rep')
''')

cur.execute('''
INSERT INTO orderDetails (priceEach, quantityOrdered, orderDate) VALUES
            (100.00, 5, '2024-01-15'),
            (50.00, 10, '2024-02-20'),
            (75.50, 3, '2024-03-10'),
            (120.00, 2, '2024-04-05'),
            (60.25, 8, '2024-05-30')
''')

conn.commit()

cur.execute("SELECT * FROM employees")
employee_data = cur.fetchall()
print(employee_data)

cur.execute("""
    SELECT employeeNumber, lastName
    FROM employees
""")
df_first_five = cur.fetchall()

cur.execute("""
    SELECT lastName, employeeNumber
    FROM employees
""")
df_five_reverse = cur.fetchall()

cur.execute("""
    SELECT lastName, employeeNumber AS ID
    FROM employees
""")
df_alias = cur.fetchall()

cur.execute("""
    SELECT
        CASE
            WHEN jobTitle = "President"
                OR jobTitle = "VP Sales"
                OR jobTitle = "VP Marketing"
            THEN "Executive"
            ELSE "Not Executive"
        END AS role
    FROM employees
""")
df_executive = cur.fetchall()

cur.execute("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees
""")
df_name_length = cur.fetchall()

cur.execute("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""")
df_short_title = cur.fetchall()

cur.execute("SELECT * FROM orderDetails")
order_details = cur.fetchall()
print(order_details)

cur.execute("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderDetails
""")
sum_total_price = sum(row[0] for row in cur.fetchall())

cur.execute("""
    SELECT
        orderDate,
        strftime('%d', orderDate) AS day,
        strftime('%m', orderDate) AS month,
        strftime('%Y', orderDate) AS year
    FROM orderDetails
""")
df_day_month_year = cur.fetchall()

conn.close()