import sqlite3

# Connect to the database created in Task 1
conn = sqlite3.connect('nyondo_stock.db')
cursor = conn.cursor()

def run_query(label, description, sql):
    print(f"\n--- Query {label}: {description} ---")
    print(f"Executing: {sql}")
    cursor.execute(sql)
    
    # For UPDATE statements (Query G), we need to commit and then verify
    if "UPDATE" in sql.upper():
        conn.commit()
        print("Update successful.")
    else:
        results = cursor.fetchall()
        for row in results:
            print(row)

# [span_1](start_span)TASK 2 QUERIES[span_1](end_span)

# Query A: Get every column of every product
run_query('A', 'All columns', 'SELECT * FROM products')

# Query B: Get only the name and price of all products
run_query('B', 'Name and Price only', 'SELECT name, price FROM products')

# Query C: Get full details of the product with id = 3
run_query('C', 'ID equals 3', 'SELECT * FROM products WHERE id = 3')

# Query D: Find all products whose name contains 'sheet' (partial match)
run_query('D', 'Name contains "sheet"', "SELECT * FROM products WHERE name LIKE '%sheet%'")

# Query E: Get all products sorted by price, highest first
run_query('E', 'Sorted by price (High to Low)', 'SELECT * FROM products ORDER BY price DESC')

# Query F: Get only the 2 most expensive products
run_query('F', 'Top 2 most expensive', 'SELECT * FROM products ORDER BY price DESC LIMIT 2')

# Query G: Update the price of Cement (id=1) to 38,000 then confirm
run_query('G', 'Update Cement price', 'UPDATE products SET price = 38000 WHERE id = 1')

# Final Verification for Query G
print("\n--- Verification for Query G ---")
cursor.execute('SELECT * FROM products WHERE id = 1')
print(cursor.fetchone())

conn.close()
