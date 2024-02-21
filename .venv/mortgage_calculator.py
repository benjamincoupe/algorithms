"""

Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest
rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for
users to select the compounding interval (Monthly, Weekly, Daily, Continually).

"""

loan_amount = int(input("Enter the value of the loan in dollars here: "))
years = int(input("Enter the duration of the loan in years here: "))
interest_rate = float(input("Enter the interest rate as a decimal here: "))

number_payments = years * 12

total_payment = (interest_rate/12 * loan_amount) / (1 - (1 / (1+interest_rate/12) **number_payments))

print(total_payment)

