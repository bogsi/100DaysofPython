year =  int(input("What is your year of birth?"))
# try:
#     if year > 1980 and year <= 1994:
#         print("You are millenial")
# except ValueError:
#     print("Unexpected Value")
#     if year > 1994:
#         print("You are gen z")

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
