num1 = 42  #data type numbers
num2 = 2.3   #data type numbers
boolean = True   #boolean
string = 'Hello World'     #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuple initialize
print(type(fruit))  #print immutable tuple
print(pizza_toppings[1])   #list access value
pizza_toppings.append('Mushrooms') #list add value
print(person['name'])    #dictionary access value
person['name'] = 'George'  #dictionary change value
person['eye_color'] = 'blue'  #dictionary add value
print(fruit[2]) #tuple access value

if num1 > 45:
    print("It's greater")       #conditional if statement
else:     
    print("It's lower")         #conditional else statement

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:          #conditional else if statement
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop start condition
    print(x)
for x in range(2,5):  #for loop stop condition
    print(x)
for x in range(2,10,3): #for loop increment condition
    print(x)
x = 0           #variable declaration
while(x < 5):   #while loop start and stop conditions
    print(x)
    x += 1      #while loop increment condition

pizza_toppings.pop()    #delete value in a list
pizza_toppings.pop(1)  #delete a specific item in a list

print(person)
person.pop('eye_color')  #dictionary delete value
print(person)

for topping in pizza_toppings:    #for loop
    if topping == 'Pepperoni':   #if statement condition
        continue                #continue for loop
    print('After 1st if statement')   
    if topping == 'Olives':
        break                   #break for loop

def print_hello_ten_times():    #function
    for num in range(10):     #function parameter
        print('Hello')        #function return

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)