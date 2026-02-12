##Prework
# Messy script to be refactored
'''users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]

# Calculate total age and count users for average
total_age = 0
user_count_for_age = 0
for user in users:
    if isinstance(user.get("age"), int):
        total_age += user["age"]
        user_count_for_age += 1
average_age = total_age / user_count_for_age
print(f"average user age: {average_age:.2f}")

# Get a list of all active user emails
active_user_emails = []
for user in users:
    if user.get("is_active") and user.get("email"):
        active_user_emails.append(user["email"])
print(f"active user emails: {active_user_emails}")
'''

##Final Code

# Sample user data
USERS = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]

def calculate_average_age(user_list: List[Dict[str, Any]]) -> float:
    """
    Calculate the average age of users from a list.
    
    Handles empty lists and non-iterable inputs gracefully.
    """
    try:
        # Extracting valid ages
        valid_ages = [u["age"] for u in user_list if isinstance(u.get("age"), int)]
        
        # This will trigger ZeroDivisionError if valid_ages is empty
        return sum(valid_ages) / len(valid_ages)

    except ZeroDivisionError:
        print("Error: Cannot calculate average age because no valid numeric ages were found.")
        return 0.0
    except TypeError:
        print("Error: Provided data is not a valid list of users.")
        return 0.0

def get_active_user_emails(user_list: List[Dict[str, Any]]) -> List[str]:
    """
    Extract emails from active users.
    
    Handles missing dictionary keys and non-iterable inputs gracefully.
    """
    active_emails = []
    try:
        for user in user_list:
            # We use .get() for 'is_active' to avoid KeyError, 
            # but we'll simulate a potential KeyError check here
            if user.get("is_active"):
                # If 'email' is missing, accessing via ['email'] would raise KeyError
                active_emails.append(user["email"])
        return active_emails

    except KeyError as e:
        print(f"Error: Missing expected data key in user record: {e}")
        return []
    except TypeError:
        print("Error: The user list provided is not iterable.")
        return []

if __name__ == "__main__":
    # Test 1: Standard Data
    print("--- Standard Data ---")
    print(f"Average Age: {calculate_average_age(USERS):.2f}")
    print(f"Active Emails: {get_active_user_emails(USERS)}")

    # Test 2: Edge Case - Empty List
    print("\n--- Testing Empty List ---")
    print(f"Average Age: {calculate_average_age([])}")

    # Test 3: Edge Case - Missing Keys
    print("\n--- Testing Missing Keys ---")
    malformed_users = [{"name": "broken", "is_active": True}] # Missing 'email'
    print(f"Active Emails: {get_active_user_emails(malformed_users)}")