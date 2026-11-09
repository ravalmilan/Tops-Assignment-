
# Brute Force Attack Simulation

# Preset PIN
correct_pin = "2580"

# Attempt counter
attempts = 0

# Try all possible 4-digit PIN combinations
for pin in range(10000):

    # Convert number into a 4-digit string
    guessed_pin = str(pin).zfill(4)

    attempts += 1

    print("Trying PIN:", guessed_pin)

    # Check whether PIN matches
    if guessed_pin == correct_pin:
        print("\nPIN Matched!")
        print("Correct PIN:", guessed_pin)
        print("Total Attempts:", attempts)
        break
