# # Use of Module:
# import datetime
# today = datetime.datetime.today()
# print(today)

# Fibonacci:
def fibonacci(n):
    new_list = [1, 1]
    if(n <= 2):
        return new_list[:n]

    first = 1
    second = 1

    i = 3
    while i <= n:
        i = i + 1
        first = second
        second = first + second
        new_list.append(second)
        
    return new_list
