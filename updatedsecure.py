import sqlite3

def validate_input(field, value):
    """Returns True if valid, False otherwise based on task rules."""
    if field == "name":
        # String, at least 2 chars, no < > or ;
        forbidden = ["<", ">", ";"]
        if not isinstance(value, str) or len(value) < 2:
            return False
        if any(char in value for char in forbidden):
            return False
            
    elif field == "price":
        # Positive number greater than 0
        try:
            if float(value) <= 0:
                return False
        except (ValueError, TypeError):
            return False
            
    elif field == "username":
        # String, no spaces, not empty
        if not isinstance(value, str) or not value or " " in value:
            return False
            
    elif field == "password":
        # String, at least 6 characters
        if not isinstance(value, str) or len(value) < 6:
            return False
            
    return True

def search_product_safe(product_name):
    if not validate_input("name", product_name):
        print("Invalid input for product name.")
        return None
    
    # Your parameterized query logic from Task 4
    # db_connection.execute("SELECT * FROM products WHERE name = ?", (product_name,))
    print(f"Success: Searching for '{product_name}'")
    return True

def login_safe(username, password):
    if not validate_input("username", username) or not validate_input("password", password):
        print("Invalid login credentials format.")
        return None
    
    # Your parameterized query logic from Task 4
    print(f"Success: Logging in user '{username}'")
    return True
if __name__ == "__main__":
    print("--- Testing Search ---")
    search_product_safe('cement')
    search_product_safe('script')
    search_product_safe('')

    print("\n---Testing Login ---")
    login_safe('ad min', 'pass123')
    login_safe('admin', 'ab')
    login_safe('admin', 'admin 123')
