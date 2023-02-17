#P1HW2
#Feb 17
#CTI-110 P1HW2 - Travel Expense
#Kendall Evans

print('This program calculates and displays travel expenses')
print('\n')

budget = input("Enter Budget: ")
print('\n')

location = input("Enter your travel destination: ")
print('\n')

fuel = input("How much do you think you will spend on gas? ")
print('\n')

accomodation = input("Approximately, how much will you need for accomodation/hotel? ")
print('\n')

food = input("Last, how much do you need for food? ")
print('\n')

print('Travel Expenses')
print('Location: ' + location)
print('Initial Budget: ' + budget)
print('\n')
print('Fuel: ' + fuel)
print('Accomodation: ' + accomodation)
print('Food: ' + food)
print('\n')
expense = int(fuel) + int(accomodation) + int(food)
balance = int(budget) - int(expense)
print('Remaining Balance: ', + balance)






