# Loop means that continue working as per conditions. As long as the condition is true. Until then it will continue.
# For example: 
studentId = ['Kajal', 'Sajal', 'Emon', 'Shukkor', 'Mannan', 'Rajib', 'Polash', 'Sajib']
for i in studentId:
    if(i == 'Kajal'):
        print("You're so cute!")
    else:
        False
print('Your task is complete!')

n1 = 0
n2 = 1
fibo = 1
i = 2
n = int(input('Enter number: '))
print(n1, n2, end='')
while(i < n):
    fibo = n1 + n2
    n1 = n2
    n2 = fibo
    print(fibo, end='')
    i = i + 1

'''
white loop, do while loop, for loop
loop, nested loop
'''