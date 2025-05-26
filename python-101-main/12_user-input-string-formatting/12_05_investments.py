# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

principal = float(input("Enter the investment amount: "))
rate_percent = float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the number of years to invest: "))

rate = rate_percent / 100

future_value = principal * (1 + rate) ** years

print(f"\nAfter {years} years, your investment will be worth: ${future_value:.2f}")