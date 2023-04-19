#Question 1
def hello_name(user_name):
    print("Hello " + user_name.upper() + "!")
    
hello_name("brett")

# Question 2
def odd_numbers():
    numbers = list(range(0, 101))
    for num in numbers:
        if num % 2 != 0:
        	print(num)
odd_numbers()

# Question 3
def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

test = max_num_in_list([2,12,56])
print(max_num_in_list([2,12,56]))

# Question 4
def is_leap(a_year):
    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)

is_leap(2020)

# Question 5
def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)
is_consecutive([1,2,3,4])
is_consecutive([1,5,3,4])