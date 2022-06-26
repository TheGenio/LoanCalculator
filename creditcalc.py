# write your code here
import argparse
from math import *



parser = argparse.ArgumentParser(description='Loan Calculator that can calculate different types of loans')
parser.add_argument('--type', help='you need to choose a loan type')
parser.add_argument('--principal', type=float, help='you need to add the loan principal')
parser.add_argument('--periods', type=int, help='you need to add the loan period')
parser.add_argument('--interest',type=float ,help='you need to add the loan interest')
parser.add_argument('--payment',type=float ,help='you need to add the loan payment')

args = parser.parse_args()

wht_calc = input()

def nom_interst(interest):
    x = (interest / (12 * 100))
    return x
def diff_pay(princ, period, interest):
    i = nom_interst(interest)
    m = 1
    Overpayment = 0
    while m <= period:
      D = ceil((princ / period) + i * (princ - (princ * (m - 1))/period))
      print(f"Month {m}: payment is {D}")
      m += 1
      Overpayment = Overpayment + D
    print(f"Overpayment = {int(Overpayment - princ)}")



if args.type == "diff":
    if args.principal is None or args.periods is None or args.interest is None:
        print("Incorrect parameters.")
    else:
        princ = args.principal
        period = args.periods
        intrest = args.interest
        diff_pay(princ, period, intrest)

elif args.type == "annuity":
    if (args.principal is None and args.periods is None) or (args.interest is None and args.payment is None):
        print("Incorrect parameters.")
    elif (args.principal is None and args.interest is None ) or ( args.periods is None and args.payment is None):
        print("Incorrect parameters.")
    elif (args.principal is None and args.payment is None) or (args.interest is None and args.periods is None):
        print("Incorrect parameters.")

    elif args.principal == None:
        annuity_pay = args.payment
        periods = args.periods
        interest_lon = args.interest
        nom_int = nom_interst(interest_lon)
        loan_prince = floor(annuity_pay / ((nom_int * pow(1 + nom_int, periods) / (pow(1 + nom_int, periods) - 1))))
        print(f"Your loan principal = {loan_prince}!")
        overpay = ceil(annuity_pay * periods - loan_prince)
        print(f"Overpayment = {int(overpay)}")

    elif args.periods == None:

        loan = args.principal
        monthly_pay = args.payment
        interest = args.interest
        nom_interest = nom_interst(interest)  # the nominal interest rate eq
        months_need = log(monthly_pay / (monthly_pay - nom_interest * loan),1 + nom_interest)  # the number of months eq
        months_tot = ceil(months_need)  # rounds it up
        years = months_tot / 12  # finds the year
        months = floor((years % 1) * 12)  # gets the months from the decibels

        if years == 0 and months == 1:  # grammer bs
            print("It will take %0.d month to repay this loan!" % (months))
        elif years == 0 and months > 1:  # grammer bs
            print("It will take %0.d months to repay this loan!" % (months))
        elif years == 1 and months == 0:  # grammer bs
            print("It will take %0.d year to repay this loan!" % (years))
        elif years == 1 and months > 1:  # grammer bs
            print("It will take %0.d year and %0.d months to repay this loan!" % (years, months))
        elif years > 1 and months == 0:  # grammer bs
            print("It will take %0.d years to repay this loan!" % (years))
        elif years >= 1:  # grammer bs
            print("It will take %0.d years and %0.d months to repay this loan!" % (years, months))
        else:  # grammer bs
            print("It will take %0.d years and %0.d months to repay this loan!" % (years, months))
        overpay = monthly_pay * months_tot - loan
        print(f"Overpayment = {int(overpay)}")

    elif args.payment == None:
        loan = args.principal
        months = args.periods
        interest = args.interest
        nom_interest = nom_interst(interest)  # the nominal interest rate eq
        annuity_pay = ceil(loan * ((nom_interest * pow(1 + nom_interest, months)) / (pow(1 + nom_interest, months) - 1)))
        print(f'Your monthly payment = {annuity_pay}!')
        overpay = annuity_pay * months - loan
        print(f"Overpayment = {int(overpay)}")



