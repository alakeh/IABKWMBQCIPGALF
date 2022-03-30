from argparse import ArgumentParser
import sys


def evaluate(stringList):
    '''
    Args: 
        stringList (float or int): The list of strings containing the postfix expressions.
    
    Returns:
        float: The result of the expression.
    '''
    stack = [] # take an empty stack
    # loop in through the string
    for i in stringList:
        if i in ["+","-","*","/"]: # if it is operator then pop two element from stack and perform the operation
            x = float(stack.pop())
            y = float(stack.pop())
            if i=="+":
                stack.append(y+x)
            elif i=="-":
                stack.append(y-x)
            elif i=="*":
                stack.append(y*x)
            else:
                stack.append(y/x)
        else:
            stack.append(i)
    return stack.pop() # return the result 

# write the main function
def main(stringList, file):
    '''
    Args: 
        Opening and reading the file containing the postfix expressions.
    
    Returns:
        float: The expression with the solution as a float.
    ''' # the file path
    file = open("postfix.txt","r") # opening and reading the file
    for line in file:
        ans = evaluate(stringList)
        print(line,"=",ans)
        
    file.close() # close the file

def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a file containing postfix expressions).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing reverse polish notation")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
