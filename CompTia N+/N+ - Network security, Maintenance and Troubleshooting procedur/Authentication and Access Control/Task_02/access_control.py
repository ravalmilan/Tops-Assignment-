
# Role-Based Access Control (RBAC)

# Define roles and their allowed resources
permissions = {
    "customer": ["order_history"],
    "restaurant_owner": ["menu_edit", "order_history"],
    "admin": ["menu_edit", "order_history", "admin_dashboard"]
}

# Function to check access
def check_access(user_role, resource):
    if user_role in permissions:
        return resource in permissions[user_role]
    return False


# Test cases
print("Customer Access:")
print(check_access("customer", "order_history"))
print(check_access("customer", "menu_edit"))

print("\nRestaurant Owner Access:")
print(check_access("restaurant_owner", "menu_edit"))
print(check_access("restaurant_owner", "admin_dashboard"))

print("\nAdmin Access:")
print(check_access("admin", "admin_dashboard"))
print(check_access("admin", "menu_edit"))
