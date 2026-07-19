# The Secure Password Hint Tool

password = input("Enter your secret password: ")

password.strip()

password_start = password[0]
password_end = password[-1]

print(f"your password Hint: it starts with {password_start} and ends with {password_end}.")