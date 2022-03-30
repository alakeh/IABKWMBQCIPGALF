import sys

def dog_years(age):
    if age < 0:
        raise ValueError("dogs can't have a negative age!")
    cy1 = 15
    cy2 = 9
    cy3 = 5
    if age == 0:
        return 0
    elif age == 1:
        return cy1
    elif age == 2:
        return cy1 + cy2
    else:
        return cy1 + cy2 + cy3 + (age - 2)
    
    
if __name__ == "__main__":
    print(dog_years(int(sys.argv[1])))