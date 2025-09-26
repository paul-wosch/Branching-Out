import json

USER_DATA = "users.json"


def load_json_data():
    """Return json data from file."""
    with open(USER_DATA, "r") as file:
        users = json.load(file)
    return users


def print_users(users):
    """Print user information for the given list of users."""
    for user in users:
        print(user)


def filter_users_by_name(name):
    """Return list of user objects filtered by name."""
    users = load_json_data()
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    print_users(filtered_users)


def filter_users_by_age(age):
    """Return list of user objects filtered by age."""
    users = load_json_data()
    filtered_users = [user for user in users if user["age"] == age]
    print_users(filtered_users)


def filter_users_by_email(email):
    """Return list of user objects filtered by name   ."""
    users = load_json_data()
    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(user)


def main():
    """Show users from a JSON file,
    with the possibility to filter by different criteria.
    """
    filter_option = input("What would you like to filter by? ('name', 'age' or 'email'): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        while True:
            try:
                age_to_search = int(input("Enter an age to filter users: ").strip())
                break
            except ValueError:
                print("Only whole numbers are allowed for the age filter.")
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email address to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
