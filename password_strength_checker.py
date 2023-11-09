# Password Strength Checker

def check_password_strength(password):
    # Criteria variables
    min_length = 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*"

    # Check minimum length
    if len(password) >= min_length:
        for char in password:
            # Check for uppercase letters
            if char.isupper():
                has_upper = True
            # Check for lowercase letters
            if char.islower():
                has_lower = True
            # Check for digits
            if char.isdigit():
                has_digit = True
            # Check for special characters
            if char in special_characters:
                has_special = True

        # Password strength evaluation
        if has_upper and has_lower and has_digit and has_special:
            print("Password is strong! Good job!")
        else:
            print("Password is weak. Please make it stronger.")
    else:
        print("Password is too short. Minimum length should be", min_length, "characters.")

# Main function
if __name__ == "__main__":
    password = input("Enter your password: ")
    check_password_strength(password)
