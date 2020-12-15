#for loops challenge 13:Factorial Calculator app
import math

print('welcom to the factorial Calculator App')

#get user input
number = int(input('\nWhat number would you like to compute the factorial of:'))

#Display the mathematical relatinoship of a factorial
print(str(number) + '!=' ',end=')
for i in range(1,number):
    print(str(i), end= '*')
    print(str(number))


#using the math library
fact = math.factorial(number)
print('\nHere is the result from the math library:')
print('the factorial of' + str(number) + 'is' + str(fact) + '!')

#using my own algorthm
fact = 1
for i in range(1,number+1):
    fact = fact*i
print('\nHERE IS THE RESULT FROM MY OWN ALGORITHM:')
print('The factorial of' + str(number) + 'is' + str(fact) + '!')

#Summary
print('\nIt is shown twice that' + str(number) + '!=' + str(fact) + '(with excitement!)')
