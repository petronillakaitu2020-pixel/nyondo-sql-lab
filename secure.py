import sqlite3
conn = sqlite3.connect('nyondo_stock.db')

def search_product_safe(name):
    # SECURE: The '?' placeholder treats input as plain text
    query = "SELECT * FROM products WHERE name LIKE ?"
    # Wrap the search term in % for the LIKE operator
    results = conn.execute(query, (f"%{name}%",)).fetchall()
    print(f"Query: {query}")
    print(f"Result: {results}\n")

def login_safe(username, password):
    # SECURE: Parameterized inputs prevent bypasses
    query = "SELECT * FROM users WHERE username=? AND password=?"
    result = conn.execute(query, (username, password)).fetchone()
    print(f"Query: {query}")
    print(f"Result: {result}\n")




# These must ALL return [] or None when you run them
print('Test 1:', search_product_safe("' OR 1=1--"))
print('Test 2:', search_product_safe("' UNION SELECT id,username,password,role FROM users--"))
print('Test 3:', login_safe("admin'--", 'anything'))
print('Test 4:', login_safe("' OR '1'='1", "' OR '1'='1"))