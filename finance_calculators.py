import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan\n")

# Asks the user for 'investment' or 'bond', saved into the 'selection' variable, any capitalisation stored as lower case and used in if statements 
selection = input("Please enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# If user writes 'investment', a number of questions are asked and stored into variables, some inputs only require integers, hence the 'int' function.
if selection == "investment":

    amount = int(input("How much money are you depositing? "))
    intr_rate = int(input("Please enter the interest rate: "))
    inv_years = int(input("How many years are you planning to invest for? "))
    interest = input("Do you want 'simple' or 'compound' interest? ")

# Simple interest calculated and rounded to two decimal places, and an informative print statement for the user.
    if interest == "simple":
        simple_interest = amount*(1 + (intr_rate/100)*inv_years)
        simple_interest2 = round(simple_interest, 2)

        print(f"With simple interest, you would earn £{simple_interest2 - amount} in {inv_years} years with {intr_rate}% interest rate.")

# Compound interest calculated and rounded to two decimal places, and an informative print statement for the user.
    if interest == "compound":
        compound_interest = amount*math.pow((1+(intr_rate/100)),inv_years)
        compound_interest2 = round(compound_interest, 2)

        print(f"With compound inerest, you would earn £{compound_interest2 - amount} in {inv_years} years with {intr_rate}% interest rate.")

# ELIF statement if user writes 'bond', number of questions are asked and stored in variables for use in the formula.
elif selection == "bond":

    housevalue = int(input("Please enter the current value of your house? "))
    bond_intr = int(input("Please enter the interest rate: "))
    no_months = int(input("Please enter the number of months you plan to repay the bond: "))

# Repayment calculation and answer rounded to two decimal places and presented to the user with a print statement.
    repayment = ((bond_intr/100)/12) * housevalue/(1 - (1 + ((bond_intr/100)/12))**(-no_months))
    repayment2 = round(repayment, 2)

    print(f"Within your repayment bond plan, you would have to repay £{repayment2} each month.")

# Error message presented if 'investment' or 'bond' (any capitalisation) not inputted from the user.
else:
    print("Please enter a valid option from the menu above.") 