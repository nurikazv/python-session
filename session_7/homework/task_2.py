# Create a function create_email(name, domain="example.com") that:
# - Defines an inner function sanitize_name() that:
#     - Converts the name to lowercase
#     - Replaces spaces with dots
#   Returns the final email.

# Example:
# print(create_email("Jon Doe"))         # "jon.doe@example.com"

def create_email(name, domain="example.com"):
    def sanitize_name():
        return name.lower().replace(" ", ".")

    return f"{sanitize_name()}@{domain}"

print(create_email("Jon Doe"))

print(create_email("Bob Smith"))
