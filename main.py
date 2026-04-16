def brute_force(password_to_crack, wordlist):
    print(" Starting brute force attack...\n")

    for attempt, password in enumerate(wordlist, start=1):
        print(f"Trying password {attempt}: {password}")

        if password == password_to_crack:
            print("\n Password FOUND!")
            print(f" Password is: {password}")
            print(f"Attempts: {attempt}")
            return

    print("\n Password not found in wordlist.")

if __name__ == "__main__":
    # Simulated real password
    real_password = "admin123"

    # Wordlist (dictionary attack)
    wordlist = [
        "123456",
        "password",
        "admin",
        "admin123",
        "qwerty",
        "letmein"
    ]

    brute_force(real_password, wordlist)
