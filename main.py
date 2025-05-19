import re

# Define Regular Expressions
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
phone_pattern = r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}'
credit_card_pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

# Simulated API Response String
api_response = """
Contact emails: jane.doe@example.com, support@company.org, hello.world@edu.co.uk
Call us at (123) 456-7890 or 987-654-3210. Also available: 123.456.7890.
Recent transactions: $1,200.99, $99.00, $7.50
Credit cards used: 1234-5678-9012-3456, 4321 8765 2109 6543
Backup email: test_email123@alustudent.com
"""

# Extract data using regex
emails = re.findall(email_pattern, api_response)
phones = re.findall(phone_pattern, api_response)
credit_cards = re.findall(credit_card_pattern, api_response)
currencies = re.findall(currency_pattern, api_response)

# Print the extracted results
print("📧 Email Addresses:", emails)
print("📱 Phone Numbers:", phones)
print("💳 Credit Card Numbers:", credit_cards)
print("💰 Currency Amounts:", currencies)
