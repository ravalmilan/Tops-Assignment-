
import random

# Hardcoded login credentials
correct_username = "admin"
correct_password = "paytm123"

# Ask user for credentials
username = input("Enter Username: ")
password = input("Enter Password: ")

# Check password
if username == correct_username and password == correct_password:

    print("\nPassword Verified!")

    # Generate a 6-digit OTP
    otp = random.randint(100000, 999999)

    # Display OTP in console
    print("Your OTP is:", otp)

    # Ask user to enter OTP
    entered_otp = int(input("Enter 6-digit OTP: "))

    # Verify OTP
    if entered_otp == otp:
        print("\nLogin Successful")
    else:
        print("\nInvalid OTP. Login Failed.")

else:
    print("\nIncorrect Username or Password.")
