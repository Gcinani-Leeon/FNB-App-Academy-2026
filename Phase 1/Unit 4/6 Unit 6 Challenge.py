balance = 1000.00

withdrawal = float(input("Enter the amount to withdraw: "))

if withdrawal <= 0:
    print("Invalid Transaction. Withdrawal amount more than R0.")
elif withdrawal >= balance:
    print(f"Invalid Transaction. Withdrawal amount exceeds your balance of R{balance}.")
elif withdrawal <= balance:
    balance = balance - withdrawal
    print(f"Withdrawal of R{withdrawal} was successful.")
    print(f"Your new balance is R{balance}.")
