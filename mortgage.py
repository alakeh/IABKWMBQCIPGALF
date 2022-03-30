"""Perform fixed-rate mortgage calculations."""

from argparse import ArgumentParser
from functools import total_ordering
import math
import sys

def get_min_payment(amount,interest,term=30,payments=12):
    '''
    get_min_payment() calculates the minimum mortagage payments.
    Args: 
        Amount is the amount of the mortgage.
        Interest is the interest rate per payment. (between 0 and 1)
        Term is the length of the mortgage. (default is set to 30 years)
        Payments is the number of payments per year. (default is 12 months)
    
    Returns:
        The solution to A = (amount * rate * (1 + rate)**n)/((1 + rate)**n - 1) will be returned as a float value.
    '''
    n = term * payments
    i = interest / payments
    A = (amount * i * (1 + i)**n)/((1 + i)**n - 1)
    return math.ceil(A)

def interest_due(balance,interest,payments=12):
  
    '''The purpose of this function is to find the interest that is due. 125,464,872/41820.6241
    Args: 
        Balance is the total mortgage balance.
        Interest is the interest rate per payment. (between 0 and 1)
        Payments is the number of payments per year. (default is set to 12 months)
    
    Returns:
        A float value solving the following equation i = br.
    '''
  
    b=balance
    r=interest/payments
  
    i=b*r
    return i

def remaining_payments(balance,interest,target,payments=12):
    '''The purpose of this function is to find the interest that is due. 125,464,872/41820.6241
    Args: 
        Balance is the total mortgage balance.
        Interest is the interest rate per payment. (between 0 and 1)
        Target is the users target payment price.
        Payments is the number of payments per year. (default is set to 12 months)
    
    Returns:
        A float value that will show the remaining payments left on the mortgage.
    '''
    counter = 0
    while balance > 0:
        totalInterest = interest_due (balance, interest, payments)

        if target < totalInterest:
            # will never be able to repay this loan, payment is too small!
            return 0

        principal = target - totalInterest
        counter+= 1
        balance -= principal
  
    return counter

def main(amount,interest,term=30,payments=12,target=None):
    minimum = get_min_payment(amount,interest,term,payments)
    if target == None:
        target = minimum
    elif payments < minimum:
        print("Your target payment is less than the minimum payment for this mortgage")
    else:
        remaining = remaining_payments(amount,interest,minimum,payments)
        print("If you make payments of {}, you will pay off the mortgage in {} payments.")

def parse_args(arglist):
    """Parse and validate command-line arguments.
    
    This function expects the following required arguments, in this order:
    
        mortgage_amount (float): total amount of a mortgage
        annual_interest_rate (float): the annual interest rate as a value
            between 0 and 1 (e.g., 0.035 == 3.5%)
        
    This function also allows the following optional arguments:
    
        -y / --years (int): the term of the mortgage in years (default is 30)
        -n / --num_annual_payments (int): the number of annual payments
            (default is 12)
        -p / --target_payment (float): the amount the user wants to pay per
            payment (default is the minimum payment)
    
    Args:
        arglist (list of str): list of command-line arguments.
    
    Returns:
        namespace: the parsed arguments (see argparse documentation for
        more information)
    
    Raises:
        ValueError: encountered an invalid argument.
    """
    # set up argument parser
    parser = ArgumentParser()
    parser.add_argument("mortgage_amount", type=float,
                        help="the total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float,
                        help="the annual interest rate, as a float"
                             " between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30,
                        help="the term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_annual_payments", type=int, default=12,
                        help="the number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float,
                        help="the amount you want to pay per payment"
                        " (default: the minimum payment)")
    # parse and validate arguments
    args = parser.parse_args()
    if args.mortgage_amount < 0:
        raise ValueError("mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("annual interest rate must be between 0 and 1")
    if args.years < 1:
        raise ValueError("years must be positive")
    if args.num_annual_payments < 0:
        raise ValueError("number of payments per year must be positive")
    if args.target_payment and args.target_payment < 0:
        raise ValueError("target payment must be positive")
    
    return args


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.mortgage_amount, args.annual_interest_rate, args.years,
         args.num_annual_payments, args.target_payment)