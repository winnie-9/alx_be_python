Monthly_income = float(input("Enter your monthly income: ")) 
Monthly_expences = float(input("Enter our total expences: "))
Monthly_savings = Monthly_income - Monthly_expences
Projected_Savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)
print("Your monthly savings are $",Monthly_savings)
print("Projected savings after one year, with interest, is: $",Projected_Savings)
