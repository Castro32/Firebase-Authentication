import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import re



cred = credentials.Certificate(r'C:\Users\fidel\Downloads\cas-authentfication-firebase-adminsdk-1ns8u-9a60283ad9.json')
firebase_admin.initialize_app(cred)


def is_valid_password(password):
    # Check for password complexity
    if len(password) < 8 or not re.search(r'\d', password) or not re.search(r'[!@#$%^&*]', password):
        return False
    return True

def is_valid_email(email):
    # Use a simple regex pattern to check email validity
    email_pattern = r'^\S+@\S+\.\S+'
    return re.match(email_pattern, email) is not None

def is_valid_phone_number(phone_number):
    # Check if the phone number includes a country code (e.g., '+1' for the United States)
    return phone_number.startswith('+')

email = input('Please enter your email address: ')

# Check if the email is valid and allow re-entry if it's not
while not is_valid_email(email):
    print('Invalid email address. Please enter a valid email.')
    email = input('Please enter your email address: ')

phone_number = input('Please enter your phone number: ')

# Check if the phone number is valid and includes the country code
while not is_valid_phone_number(phone_number):
    print('Invalid phone number. Please include the country code (e.g., +1 for the United States).')
    phone_number = input('Please enter your phone number: ')

password = input('Please enter your password: ')

# Check if the password is valid and allow re-entry if it's not
while not is_valid_password(password):
    print('Invalid password. It should be at least 8 characters long and include numbers and special characters.')
    password = input('Please enter your password: ')

try:
    # Attempt to create the user
    user = auth.create_user(
        email=email,
        password=password,
        phone_number=phone_number
    )
    print('User created successfully: {0}'.format(user.uid))
except auth.EmailAlreadyExistsError:
    print('This email is already in use. Please use another email.')
except auth.AuthError as e:
    # Handle other Firebase-specific errors
    error_message = 'An error occurred while signing up. Please try again later.'
    if e.detail.get('message') == 'INVALID_PHONE_NUMBER':
        error_message = 'Invalid phone number. Please provide a valid one.'
    print('Error:', error_message)


user=auth.create_user(email = email, password = password, phone_number=phone_number)

print("User created successfully : {0}".format(user.uid))