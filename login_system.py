def login_system():
    users = {
        "admin": "1234",
        "david": "pass123",
        "mary": "hello"
    }

    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users:
            if password == users[username]:
                print("Login successful!")
                return
            else:
                print("Wrong password.")
        else:
            print("Username not found.")

        attempts += 1
        print(f"Attempts remaining: {max_attempts - attempts}")

    print("Account locked. Maximum attempts reached.")


login_system()