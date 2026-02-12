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
from typing import List, Dict, Any

# Global constant for user data
USERS = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]

def calculate_average_age(user_list: List[Dict[str, Any]]) -> float:
    """
    Calculate the average age of users from a list, ignoring non-integer values.

    Parameters
    ----------
    user_list : List[Dict[str, Any]]
        A list of dictionaries where each dictionary represents a user.

    Returns
    -------
    float
        The average age of users. Returns 0.0 if no valid ages are found or
        if an error occurs.
    """
    try:
        # Filter for valid integer ages
        valid_ages = [u["age"] for u in user_list if isinstance(u.get("age"), int)]
        
        # Calculate average; triggers ZeroDivisionError if valid_ages is empty
        return sum(valid_ages) / len(valid_ages)

    except ZeroDivisionError:
        print("error: cannot calculate average age of an empty list.")
        return 0.0
    except (TypeError, AttributeError):
        print("error: provided data is not a valid list of user dictionaries.")
        return 0.0

def get_active_user_emails(user_list: List[Dict[str, Any]]) -> List[str]:
    """
    Extract emails from users who are currently active and have an email provided.

    Parameters
    ----------
    user_list : List[Dict[str, Any]]
        A list of dictionaries where each dictionary represents a user.

    Returns
    -------
    List[str]
        A list of email addresses for active users.
    """
    active_emails = []
    try:
        for user in user_list:
            # Check if user is active; using .get() to avoid KeyError here
            if user.get("is_active"):
                # Accessing 'email' directly to trigger KeyError if missing
                active_emails.append(user["email"])
        return active_emails

    except (KeyError, AttributeError, TypeError) as e:
        print(f"error: issue processing user records: {e}")
        return []

if __name__ == "__main__":
    # Calculate and display the average age
    avg_age = calculate_average_age(USERS)
    print(f"average user age: {avg_age:.2f}")

    # Retrieve and display active emails
    active_emails = get_active_user_emails(USERS)
    print(f"active user emails: {active_emails}")