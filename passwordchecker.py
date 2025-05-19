import re

def is_valid_email(email):
    # Define a regex pattern for a valid email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-u]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

def main():
    print("Welcome to the Email Format Checker!")
    email = input("Please enter your email address: ")
    
    if is_valid_email(email):
        print("The email format is valid.")
    else:
        print("Invalid email format. Please try again.")

if __name__ == "__main__":
    main()