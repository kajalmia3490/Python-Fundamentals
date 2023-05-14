# Function means that is organized and reuseable a specific block of code. In which a independent small part of a big program. Which has a specific name. Which consists one or more statements.
# For example: 
def greetings(str):
    print(str)

greetings('Hello, Kajal!')

name = input('Enter your new name: ')
def name_called(greating):
    num1 = 10
    num2 = 20
    sum = num1 + num2
    print('Hello Mr.', greating,'! Welcome')
    print('Your sumation is: ', sum)
name_called(name)