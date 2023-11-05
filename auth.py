import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import re
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from firebase_admin import credentials, initialize_app, auth

def is_valid_password(password):
    if len(password) < 8 or not re.search(r'\d', password) or not re.search(r'[!@#$%^&*]', password):
        return False
    return True

def is_valid_email(email):
    email_pattern = r'^\S+@\S+\.\S+'
    return re.match(email_pattern, email) is not None

def is_valid_phone_number(phone_number):
    return phone_number.startswith('+')


cred = credentials.Certificate(r'C:\Users\fidel\Downloads\cas-authentfication-firebase-adminsdk-1ns8u-9a60283ad9.json')
initialize_app(cred)


window = tk.Tk()
window.title("Firebase User Registration")
window.geometry("600x500")
window.resizable(False, False)


email = simpledialog.askstring("Email Input", "Please enter your email address: ")

while not is_valid_email(email):
    print('Invalid email address. Please enter a valid email.')
    email = simpledialog.askstring("Email Input", "Please enter your email address: ")

phone_number = simpledialog.askstring("Phone number input", "Please enter your phone number: ")

while not is_valid_phone_number(phone_number):
    print('Invalid phone number. Please include the country code (e.g., +1 for the United States).')
    phone_number = simpledialog.askstring("Phone number input", "Please enter your phone number: ")

password = simpledialog.askstring("Enter the password", "Please enter your password: ")

while not is_valid_password(password):
    print('Invalid password. It should be at least 8 characters long and include numbers and special characters.')
    password = simpledialog.askstring("Enter the password", "Please enter your password: ")

try:
    user = auth.create_user(
        email=email,
        password=password,
        phone_number=phone_number
    )
    print('User created successfully: {0}'.format(user.uid))
except auth.EmailAlreadyExistsError:
    print('This email is already in use. Please use another email.')
except auth.AuthError as e:
    error_message = 'An error occurred while signing up. Please try again later.'
    if e.detail.get('message') == 'INVALID_PHONE_NUMBER':
        error_message = 'Invalid phone number. Please provide a valid one.'
    print('Error:', error_message)

window.mainloop()
