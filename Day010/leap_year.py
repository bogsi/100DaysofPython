def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    # Year has 365 days; Leap year has 366 days
    """"""
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(is_leap_year(input("Enter Year: ")))
