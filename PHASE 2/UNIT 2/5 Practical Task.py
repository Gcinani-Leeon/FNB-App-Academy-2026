# string_formatter.py

name = input("Enter your name: ")
last_name = input("Enter your last name: ")
bio_message = input("Enter a short bio message: ")

username = name[0] + last_name.lower()

username = username.title()
bio_message = bio_message.strip()
bio_message = bio_message.replace("i am", "i'm")

bio_len = len(bio_message)

print()
print(f"Username: {username} ")
print(f"Bio Message: {bio_message} ")
print(f"Bio Length: {bio_len} ")
