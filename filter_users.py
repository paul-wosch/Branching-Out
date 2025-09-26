import json

USER_DATA = "users.json"


def load_json_data():
    """Return json data from file."""
    with open(USER_DATA, "r", encoding="utf-8") as file:
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
    print_users(filtered_users)


FILTER_OPTIONS = {"name": filter_users_by_name,
                  "age": filter_users_by_age,
                  "email": filter_users_by_email
                  }


def ask_for_filter():
    """Ask the user to select one of the available filter options
    and return this value.
    """
    filter_options = [f"'{key}'" for key, _ in FILTER_OPTIONS.items()]
    filter_options_str = ", ".join(filter_options)
    while True:
        filter_option = input(f"What would you like to filter by?"
                              f" ({filter_options_str}): ").strip().lower()
        if FILTER_OPTIONS.get(filter_option):
            break
        if not filter_option:
            print("Please enter one of the above filter options.")
        else:
            print("Filtering by that option is not yet supported.")
    return filter_option


def ask_for_search_term(filter_option):
    """Ask the user to enter a search / filter term
    and return this value.
    """
    while True:
        search_term = input(f"Enter a/an {filter_option} to filter users: ").strip()
        if filter_option == "age" and search_term.isdigit():
            search_term = int(search_term)
            break
        if filter_option == "age":
            print("Only whole numbers are allowed for the age filter.")
        else:
            break
    return search_term


def do_filter(filter_option, search_term):
    """Call the appropriate function for the given filter option
    utilizing a dispatch table."""
    return FILTER_OPTIONS[filter_option](search_term)


def main():
    """Show users from a JSON file,
    with the possibility to filter by different criteria.
    """
    filter_option = ask_for_filter()
    search_term = ask_for_search_term(filter_option)
    do_filter(filter_option, search_term)


if __name__ == "__main__":
    main()
