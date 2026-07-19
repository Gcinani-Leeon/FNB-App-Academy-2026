# Student Info Formatter

first_name = input("Enter your first name: ")
surname = input("Enter yout surname: ")
age = int(input("Wtat's your Age this year?: "))
favourite_number = input("What's your favourite number?: ")

first_name = first_name.upper()
surname = surname.title()
age_months = int(age) * 12
age_months = round(age_months, 2)

print(f"Hello {first_name} {surname}, You are {age_months} months old({age} years) and your favourite number is => {favourite_number}.")
print()
print(f"first name type: {type(first_name)}")
print(f"surname type: {type(surname)}")
print(f"age type: {type(age)}")
print(f"favourite number type: {type(favourite_number)}")